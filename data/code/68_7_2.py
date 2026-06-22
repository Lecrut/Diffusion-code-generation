def dollars_to_cents(dollars):
    if dollars < 0:
        return -int(abs(dollars) * 100 + 0.5)
    return int(dollars * 100 + 0.5)

if __name__ == '__main__':
    print(dollars_to_cents(1.67))
    print(dollars_to_cents(0.1 + 0.2))
    print(dollars_to_cents(10))
    print(dollars_to_cents(-5.345))