def dollars_to_cents(dollars):
    if dollars < 0:
        return -int(abs(dollars * 100 + 0.5))
    return int(dollars * 100 + 0.5)

if __name__ == '__main__':
    print(dollars_to_cents(10.50))
    print(dollars_to_cents(0.01))
    print(dollars_to_cents(-5.25))
    print(dollars_to_cents(0.00))
    print(dollars_to_cents(123.456))
    print(dollars_to_cents(-0.005))