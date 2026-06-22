from decimal import Decimal, getcontext

def km_to_m(kilometers):
    if isinstance(kilometers, str):
        km = Decimal(kilometers)
    elif isinstance(kilometers, (int, float)):
        km = Decimal(str(kilometers))
    elif isinstance(kilometers, Decimal):
        km = kilometers
    else:
        raise TypeError("Unsupported type for kilometers")
    
    meters = km * Decimal('1000')
    return meters

if __name__ == '__main__':
    result1 = km_to_m('1.1')
    print(result1)
    
    result2 = km_to_m(Decimal('2.5'))
    print(result2)
    
    result3 = km_to_m(5)
    print(result3)