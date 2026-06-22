def dollars_to_cents(dollars: float) -> int:
    if dollars < 0:
        return -int(-dollars * 100)
    return int(dollars * 100)

if __name__ == '__main__':
    print(dollars_to_cents(1.23))
    print(dollars_to_cents(-1.23))
    print(dollars_to_cents(0.0))
    print(dollars_to_cents(0.99))
    print(dollars_to_cents(-0.99))