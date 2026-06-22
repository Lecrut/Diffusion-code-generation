def dollars_to_cents(dollars):
    return int(dollars * 100)

if __name__ == '__main__':
    sample_values = [10.5, -3.75, 0.0, 100, -0.01]
    for value in sample_values:
        print(dollars_to_cents(value))