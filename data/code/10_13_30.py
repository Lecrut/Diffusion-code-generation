import decimal

def compare_temperatures(temp1, temp2):
    getcontext().prec = 50
    d_temp1 = Decimal(str(temp1))
    d_temp2 = Decimal(str(temp2))
    if d_temp1 < d_temp2:
        return 'less than'
    elif d_temp1 > d_temp2:
        return 'greater than'
    else:
        return 'equal'
if __name__ == '__main__':
    temp1 = 36.6
    temp2 = 36.6
    result = compare_temperatures(temp1, temp2)
    print(result)