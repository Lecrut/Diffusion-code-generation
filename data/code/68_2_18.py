def dollars_to_cents(dollars: float) -> int:
    return int(round(dollars * 100))

if __name__ == '__main__':
    sample_values = [12.34, -5.67, 0.005, 100.0]
    for val in sample_values:
        result = dollars_to_cents(val)
        print(result)