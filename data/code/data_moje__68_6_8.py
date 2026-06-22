def dollars_to_cents(dollars):
    return int(round(dollars * 100))

if __name__ == '__main__':
    print(dollars_to_cents(0.015))
    print(dollars_to_cents(0.025))
    print(dollars_to_cents(1.995))
    print(dollars_to_cents(100.0))
    print(dollars_to_cents(0.1))