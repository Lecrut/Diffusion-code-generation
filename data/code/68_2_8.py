def dollars_to_cents(dollars):
    return int(dollars * 100 + (0 if dollars >= 0 else -0.5))

if __name__ == '__main__':
    print(dollars_to_cents(12.34))
    print(dollars_to_cents(-12.34))
    print(dollars_to_cents(0.005))
    print(dollars_to_cents(-0.005))
    print(dollars_to_cents(0.0))