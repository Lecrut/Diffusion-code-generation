def process_csv_string(input_string):
    for part in input_string.split(','):
        stripped = part.strip()
        if stripped:
            yield stripped

if __name__ == '__main__':
    sample_input = "  apple , banana , , cherry ,  , date "
    result_generator = process_csv_string(sample_input)
    print(list(result_generator))