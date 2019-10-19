def question01(initialLevelOfDebt, interestPercentage, repaymentPercentage):
    # modify and then return the variable below
    deposit = 0.1 * initialLevelOfDebt #fixed, to be added at the end
    #interestAmount = interestPercentage * initialLevelOfDebt #variable
    currentDebt = initialLevelOfDebt 
    repaymentAmount = repaymentPercentage * initialLevelOfDebt / 100 #fixed
    if repaymentAmount < 50:
        repaymentAmount = 50
    numberOfPayments = 0
    while(currentDebt>50):
        interestAmount = interestPercentage/100 * currentDebt
        currentDebt = round(currentDebt + interestAmount - repaymentAmount)
        numberOfPayments += 1
    answer = int((numberOfPayments*repaymentAmount) + (currentDebt) + (deposit))
    return answer