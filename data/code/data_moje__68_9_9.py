def convert_dollars_to_cents(dollars_list):
    return [int(d * 100) for d in dollars_list]

if __name__ == '__main__':
    sample_values = [1.23, 4.56, 7.89, 0.01, 100.00]
    result = convert_dollars_to_cents(sample_values)
    print(result)