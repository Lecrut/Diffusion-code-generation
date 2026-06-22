def dollars_to_cents(dollars):
    dollar_str = str(dollars)
    cents_str = dollar_str.replace('.', '')
    return int(cents_str)

if __name__ == '__main__':
    print(dollars_to_cents(12.34))
    print(dollars_to_cents(0.99))
    print(dollars_to_cents(100.00))
    print(dollars_to_cents(5.1))