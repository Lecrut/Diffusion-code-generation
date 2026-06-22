def dollars_to_cents(dollars):
    return int(round(dollars * 100))

if __name__ == '__main__':
    print(dollars_to_cents(1.00))
    print(dollars_to_cents(1.005))
    print(dollars_to_cents(1.006))
    print(dollars_to_cents(0.995))
    print(dollars_to_cents(2.345))
    print(dollars_to_cents(-1.505))