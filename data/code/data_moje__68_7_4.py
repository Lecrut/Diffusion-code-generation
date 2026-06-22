import math

def dollars_to_cents(dollars: float) -> int:
    sign = 1
    if dollars < 0:
        sign = -1
        dollars = -dollars
    cents = int(math.floor(dollars * 100 + 0.5)) * sign
    return cents

if __name__ == '__main__':
    print(dollars_to_cents(12.345))
    print(dollars_to_cents(0.001))
    print(dollars_to_cents(-10.555))
    print(dollars_to_cents(0.0))
    print(dollars_to_cents(99.995))