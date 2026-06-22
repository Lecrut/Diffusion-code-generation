from decimal import Decimal, InvalidOperation

def dollars_to_cents(dollars_str):
    d = Decimal(dollars_str)
    return int(d * 100)
if __name__ == '__main__':
    result = dollars_to_cents('12.50')
    print(result)