def dollars_to_cents(amount):
    return int(abs(amount * 100))

if __name__ == '__main__':
    print(dollars_to_cents(-12.34))
    print(dollars_to_cents(0.01))
    print(dollars_to_cents(10.50))