def dollars_to_cents(amount):
    return int(round(amount * 100))

if __name__ == '__main__':
    print(dollars_to_cents(12.99))
    print(dollars_to_cents(0.01))
    print(dollars_to_cents(100.00))