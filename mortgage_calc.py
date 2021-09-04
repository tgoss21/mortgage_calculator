
# interest_rate = input(float('Enter interest rate:'))
# loan_term = input(int('Enter loan term in years: '))
# principal = input(int('Enter cost of the home: '))
# down_payment = inpput(int('Enter personal down payment: '))

interest_rate = float(6.5)
loan_term = 30
principal = 200000
down_payment = 0

def get_interest_rate(rate):
    if rate == 0 or rate < -1 or rate > 9:
        print('Invalid Interest Rate: Rate too high ot too less than 0.')
    return (rate/100)/12

def get_loan_term(years):
    return -years * 12

def get_principal(principal):
    return principal - down_payment
    
def get_monthly_payment(rate, years, principal):
    annual_rate = get_interest_rate(rate) * principal
    interest_rate = get_interest_rate(rate)
    compound_interest = annual_rate / (1 - (1 + (interest_rate))**(get_loan_term(years)))
    return round(compound_interest,2)
    
monthly_pmt = get_monthly_payment(interest_rate, loan_term, principal)

print(monthly_pmt)