#
#    Actual annuity function
#

def annuity(term, interest, adv_arr, adv_arr_str, adv_arr_out, pv_av, pv_av_str, pv_av_out, freq):
    '''
    Takes in term, interest rate, time of payment, and frequency and outputs the sum
    '''
    
    
    sum = 0
    for i in range(1,term+1):
    	sum += (1/((1+interest)**((i - adv_arr))/freq))/freq

    if input_pv_av == 1:
    	sum *= (1+interest)**term

        
    
    print(f'The {pv_av_out} of a {term}-year annuity, payable in {adv_arr_out} at a rate of interest of {interest*100}% is: {sum}')

#
#    Set up inital variables
#

    
input_adv_arr = 0
input_pv_av = 0
output_adv_arr = 'arrears'
output_pv_av = 'present value'

while True:
    
    input_interest = int(input('\nPlease state the interest rate in (percent): '))/100
    input_term = int(input('\nPlease state the term (in years): '))
    input_adv_arr_str = input("\nIs the annuity payable in advance or in arrears? (type 'adv' or 'arr')")
    input_pv_av_str = input("\nAre you looking for the accumulated value or the present value? (type 'pv' or 'av')")
    input_freq = int(input('\nHow often will this annuity be paid? (eg enter 2 for half-yearly, 4 for quarterly, 12 for monthly etc) '))


    if input_adv_arr_str == 'adv':
        input_adv_arr = 1
        output_adv_arr = 'advance'

    if input_pv_av_str == 'av':
        input_pv_av = 1
        output_pv_av = 'accumulated value'


    #
    #   Run function
    #
    annuity(input_term, input_interest, input_adv_arr, input_adv_arr_str, output_adv_arr, input_pv_av, input_pv_av_str, output_pv_av, input_freq)

    rply = input("Enter 'y' to calculate another or anything else to quit: ")
    
    if rply[0] != 'y':
        break
    else:
        continue