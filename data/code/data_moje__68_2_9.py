def dollars_to_cents(dollars):
    if dollars >= 0:
        return int(dollars * 100 + 0.5)
    else:
        return int(dollars * 100 - 0.5)

if __name__ == '__main__':
    sample_values = [10.5, -10.5, 0.01, -0.01, 100.999, -100.999]
    for val in sample_values:
        print(f"{val} dollars is {dollars_to_cents(val)} cents")