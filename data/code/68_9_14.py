def convert_dollars_to_cents(dollars_list):
    return [int(d * 100) for d in dollars_list]

if __name__ == '__main__':
    sample_values = [1.99, 10.50, 0.10, 100.0]
    result = convert_dollars_to_cents(sample_values)
    print(result)