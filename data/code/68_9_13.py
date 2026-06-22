def dollars_to_cents(dollars):
    return int(dollars * 100)

def convert_list(values):
    return [dollars_to_cents(val) for val in values]

if __name__ == '__main__':
    sample_data = [10.50, 20.99, 0.01, 100.00, 5.75]
    result = convert_list(sample_data)
    print(result)