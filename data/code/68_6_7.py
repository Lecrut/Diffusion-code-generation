def to_cents(dollars):
    return round(dollars * 100)

if __name__ == '__main__':
    print(to_cents(10.5))
    print(to_cents(10.55))
    print(to_cents(10.549))
    print(to_cents(-2.5))
    print(to_cents(0.005))