def dollar_to_cents(dollars):
    return int(abs(dollars * 100))

if __name__ == '__main__':
    print(dollar_to_cents(10.50))
    print(dollar_to_cents(-5.25))
    print(dollar_to_cents(0.01))
    print(dollar_to_cents(0))