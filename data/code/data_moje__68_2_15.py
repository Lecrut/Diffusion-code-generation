def dollars_to_cents(dollars):
    return int(round(dollars * 100))

if __name__ == '__main__':
    print(dollars_to_cents(12.34))
    print(dollars_to_cents(-5.67))
    print(dollars_to_cents(0.01))
    print(dollars_to_cents(-0.01))