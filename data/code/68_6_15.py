def dollars_to_cents(dollars):
    return int(round(dollars * 100))

if __name__ == '__main__':
    print(dollars_to_cents(10.555))
    print(dollars_to_cents(10.545))
    print(dollars_to_cents(10.55))
    print(dollars_to_cents(0.01))
    print(dollars_to_cents(0))