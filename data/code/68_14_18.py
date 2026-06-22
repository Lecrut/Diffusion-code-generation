def convert_dollars_to_cents(dollars):
    return int(dollars * 100)

if __name__ == '__main__':
    test_values = [1.0, 2.5, 10.99, 0.01]
    for val in test_values:
        result = convert_dollars_to_cents(val)
        print(f"{val} dollars is {result} cents")