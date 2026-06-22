def dollars_to_cents(dollars):
    return abs(int(dollars * 100))

if __name__ == '__main__':
    print(dollars_to_cents(12.345))
    print(dollars_to_cents(-5.67))
    print(dollars_to_cents(0.0))
    print(dollars_to_cents(100))
    print(dollars_to_cents(-0.01))