from decimal import Decimal, getcontext, ROUND_HALF_UP

def convert_dollars_to_cents(dollars: float) -> int:
    getcontext().prec = 20
    d = Decimal(str(dollars))
    return int(d * 100)

if __name__ == '__main__':
    sample_dollars = 19.99
    result = convert_dollars_to_cents(sample_dollars)
    print(result)