def dollars_to_cents(dollars: float) -> int:
    return int(dollars * 100)

if __name__ == '__main__':
    sample_value = 12.34
    print(dollars_to_cents(sample_value))