def dollars_to_cents(dollars):
    return int(round(dollars * 100))

if __name__ == '__main__':
    print(dollars_to_cents(10.505))
    print(dollars_to_cents(10.50))
    print(dollars_to_cents(10.5))