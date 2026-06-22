def dollars_to_cents(dollars):
    return int(dollars * 100)

if __name__ == '__main__':
    print(dollars_to_cents(1.23))
    print(dollars_to_cents(0.01))
    print(dollars_to_cents(100.0))