def parse_csv_optimized(csv_string):
    if not csv_string:
        return []
    values = [item.strip() for item in csv_string.split(',')]
    typed_values = []
    for value in values:
        try:
            typed_values.append(int(value))
        except ValueError:
            typed_values.append(value)
    return typed_values
if __name__ == '__main__':
    sample_string = " 10 , 25, 30 , 45 , 50 "
    result = parse_csv_optimized(sample_string)
    print(result)