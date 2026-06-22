def dollars_to_cents(dollars):
    return int(round(dollars * 100))

if __name__ == '__main__':
    print(dollars_to_cents(10.0))
    print(dollars_to_cents(10.01))
    print(dollars_to_cents(10.995))
    print(dollars_to_cents(-5.5))