def dollars_to_cents(dollars):
    return int(round(dollars * 100))

if __name__ == '__main__':
    sample_values = [1.005, 2.005, 3.5, 0.005, 0.015]
    for val in sample_values:
        result = dollars_to_cents(val)
        print(result)