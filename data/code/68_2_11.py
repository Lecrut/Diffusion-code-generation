def dollars_to_cents(dollars):
    return int(dollars * 100 + (0 if dollars >= 0 else 1 if dollars * 100 != int(dollars * 100) else 0))

def dollars_to_cents_correct(dollars):
    import math
    if dollars >= 0:
        return int(math.floor(dollars * 100 + 0.5))
    else:
        return -int(math.floor(abs(dollars) * 100 + 0.5))

def dollars_to_cents_v2(dollars):
    return int(round(dollars * 100))

if __name__ == '__main__':
    print(dollars_to_cents_v2(10.5))
    print(dollars_to_cents_v2(-10.5))
    print(dollars_to_cents_v2(0.01))
    print(dollars_to_cents_v2(-0.01))
    print(dollars_to_cents_v2(100.0))