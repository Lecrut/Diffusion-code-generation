def dollars_to_cents(amount):
    return abs(int(round(amount * 100)))

if __name__ == '__main__':
    print(dollars_to_cents(10.50))
    print(dollars_to_cents(-2.75))
    print(dollars_to_cents(0))