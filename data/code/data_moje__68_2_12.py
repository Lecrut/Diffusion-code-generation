def dollars_to_cents(dollars):
    if dollars >= 0:
        return int(dollars * 100 + 0.5)
    else:
        return -int(-dollars * 100 + 0.5)

if __name__ == '__main__':
    sample_values = [12.34, -12.34, 0.0, 100.0, -0.01]
    for value in sample_values:
        print(dollars_to_cents(value))