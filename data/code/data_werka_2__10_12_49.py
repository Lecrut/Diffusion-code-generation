import decimal

def compare_temperatures(temp1, temp2):
    decimal.getcontext().prec = 50
    dec_temp1 = decimal.Decimal(str(temp1))
    dec_temp2 = decimal.Decimal(str(temp2))
    if dec_temp1 < dec_temp2:
        return 'less than'
    elif dec_temp1 > dec_temp2:
        return 'greater than'
    else:
        return 'equal'
if __name__ == '__main__':
    temp1 = 36.6
    temp2 = 36.6
    result = compare_temperatures(temp1, temp2)
    print(result)