import decimal

def compare_temperatures(temp1, temp2):
    dtemp1 = decimal.Decimal(str(temp1))
    dtemp2 = decimal.Decimal(str(temp2))
    if dtemp1 < dtemp2:
        return 'less than'
    elif dtemp1 > dtemp2:
        return 'greater than'
    else:
        return 'equal'
if __name__ == '__main__':
    temp1 = 36.6
    temp2 = 36.6
    result = compare_temperatures(temp1, temp2)
    print(result)