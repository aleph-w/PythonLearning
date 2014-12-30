# This is a way to optimize repayment of multiple loans
# of multiple terms at multiple rates. It will make 
# suggestions on when/where to allocate free capital
# to minimize expenditures as well as money spent
# paying interest.

# As of right now, it only calculates what your current monthly payment is

loanList = []
rateList = []
termList = []
pmtList = []
newPmt = []
totalPmts = []
totalInterest = []

def getNumLoans():
    try:
        number = int(raw_input("How many loans do you have? "))
    except:
        print "Please enter a number."
        number = getNumLoans()
    if number > 10:
        print "That's too many. Try Again"
        number = getNumLoans()
    return number

    
def getLoan():
    try:
        loanAmt = float(raw_input("Enter total loan amount: "))
    except:
        print "Invalid entry"
        loanAmt = getLoan()
    return loanAmt
	
def getIntRate():
    try:
        intRate = float(raw_input("Enter annual interest rate: "))
    except:
        print "Invalid interest rate."
        intRate = getIntRate()        
    return intRate
	
def getTerm():
    try:
        termLength = int(raw_input("Enter term length in years: "))
    except:
        print "Invalid entry."
        termLength = getTerm()
    return termLength

def getCapital():
    try:
        capital = float(raw_input("How much capital do you have? "))
    except:
        print "Enter a number."
        capital = getCapital()
    return capital
		
def calcLoanPayment(principal, interestRate, term):
	startValue = principal
	numPayments = term * 12
	monthlyInterest = (interestRate/100) / 12.0
	monthlyPayment = startValue * (monthlyInterest / (1 - (1 + monthlyInterest) ** ( - numPayments)))
	return monthlyPayment
 
def createLoansList():
    for n in range(0,numLoans):
        print "For loan number %i" % int(n+1)
        loanList.append(getLoan())
        rateList.append(getIntRate())
        termList.append(getTerm())
        pmtList.append(calcLoanPayment(loanList[n],rateList[n],termList[n]))
        totalPmts.append(termList[n]*12*pmtList[n])
        totalInterest.append(totalPmts[n] - loanList[n])
        
# Deprecated - do not use
'''
def calcWithCapital():
    cap = getCapital()
    index = rateList.index(min(rateList))
'''    

numLoans = getNumLoans()
createLoansList()
print "Your total monthly payment for all %i loans will be $%s" % (numLoans, str(round(sum(pmtList),2)))
print "Your total payments for all %i loans over their life will be $%s" % (numLoans, str(round(sum(totalPmts),2)))
print "And you will pay $%s in interest." % str(round(sum(totalInterest),2))
