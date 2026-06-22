def dollars_to_cents(dollars):
    if dollars < 0:
        return -int(round(-dollars * 100, 0))
    return int(round(dollars * 100, 0))

if __name__ == '__main__':
    print(dollars_to_cents(1.235))
    print(dollars_to_cents(10.00))
    print(dollars_to_cents(0.005))
    print(dollars_to_cents(100.495))
    print(dollars_to_cents(-2.555))