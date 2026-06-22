def dollars_to_cents(dollars: float) -> int:
    return int(dollars * 100)

if __name__ == '__main__':
    print(dollars_to_cents(12.34))
    print(dollars_to_cents(5.0))
    print(dollars_to_cents(0.99))