def dollars_to_cents(amount):
    return int(round(amount * 100))

if __name__ == '__main__':
    print(dollars_to_cents(10.50))
    print(dollars_to_cents(0.005))
    print(dollars_to_cents(1.235))
    print(dollars_to_cents(1.234))