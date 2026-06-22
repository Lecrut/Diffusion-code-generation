def dollars_to_cents(dollars):
    return int(round(dollars * 100))

if __name__ == '__main__':
    print(dollars_to_cents(10.505))
    print(dollars_to_cents(10.504))
    print(dollars_to_cents(10.506))
    print(dollars_to_cents(0.005))
    print(dollars_to_cents(0.004))
    print(dollars_to_cents(0.006))