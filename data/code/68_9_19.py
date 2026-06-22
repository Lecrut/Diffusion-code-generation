def dollars_to_cents(dollars):
    return int(dollars * 100)

def process_large_list(amounts):
    return [dollars_to_cents(amount) for amount in amounts]

if __name__ == '__main__':
    sample_values = [10.5, 20.99, 0.01, 100.00, 5.555]
    converted_values = process_large_list(sample_values)
    print(converted_values)