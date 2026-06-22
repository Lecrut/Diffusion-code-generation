def dollars_to_cents(dollars):
    return int(dollars * 100)

def process_list(amounts):
    return [dollars_to_cents(val) for val in amounts]

if __name__ == '__main__':
    sample_values = [10.0, 5.5, 0.99, 100.05, 0.01]
    results = process_list(sample_values)
    print(results)