def dollars_to_cents(dollars):
    if dollars < 0:
        return int(dollars * 100)
    return int(dollars * 100)

if __name__ == '__main__':
    print(dollars_to_cents(10.5))
    print(dollars_to_cents(-10.5))
    print(dollars_to_cents(0.01))
    print(dollars_to_cents(-0.01))
    print(dollars_to_cents(0))