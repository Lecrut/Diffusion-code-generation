def dollars_to_cents(dollars):
    return abs(int(dollars * 100))

if __name__ == '__main__':
    print(dollars_to_cents(-10.50))
    print(dollars_to_cents(5.75))
    print(dollars_to_cents(0))