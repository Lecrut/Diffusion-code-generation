import decimal

def compare_temperatures(temp1, temp2):
    precision = decimal.Decimal('1e-9')
    d_temp1 = decimal.Decimal(str(temp1))
    d_temp2 = decimal.Decimal(str(temp2))
    
    if abs(d_temp1 - d_temp2) < precision:
        return 'equal'
    elif d_temp1 < d_temp2:
        return 'less than'
    else:
        return 'greater than'

if __name__ == '__main__':
    temperature1 = 40.6000000005
    temperature2 = 40.6
    relationship = compare_temperatures(temperature1, temperature2)
    print(relationship)