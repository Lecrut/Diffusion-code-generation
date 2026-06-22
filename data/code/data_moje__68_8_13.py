def dollars_to_cents(dollars):
    return int(abs(dollars * 100))

if __name__ == '__main__':
    sample_values = [1.23, -4.56, 0, 100.999, -0.01]
    for value in sample_values:
        print(dollars_to_cents(value))