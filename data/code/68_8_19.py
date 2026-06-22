def dollars_to_cents(amount):
    return abs(int(amount * 100))

if __name__ == '__main__':
    print(dollars_to_cents(-1.23))
    print(dollars_to_cents(1.23))
    print(dollars_to_cents(0.01))