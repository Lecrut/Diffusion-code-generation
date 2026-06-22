def dollars_to_cents(dollars):
    s = str(dollars)
    s = s.replace('.', '')
    return int(s)

if __name__ == '__main__':
    print(dollars_to_cents(10.00))
    print(dollars_to_cents(0.99))
    print(dollars_to_cents(123.45))
    print(dollars_to_cents(0.01))
    print(dollars_to_cents(100.00))