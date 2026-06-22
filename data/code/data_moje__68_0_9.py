def to_cents(amount):
    return round(amount * 100)

if __name__ == '__main__':
    print(to_cents(10.01))
    print(to_cents(0.29))
    print(to_cents(19.99))
    print(to_cents(100.005))