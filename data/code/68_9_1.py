def dollars_to_cents(dollars):
    return int(dollars * 100)

def convert_list_of_dollars(dollar_list):
    return [dollars_to_cents(d) for d in dollar_list]

if __name__ == '__main__':
    sample_values = [10.50, 20.05, 0.99, 100.00, 0.01]
    result = convert_list_of_dollars(sample_values)
    print(result)