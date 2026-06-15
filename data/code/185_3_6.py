def parse_csv_optimized(csv_string):
    values = []
    for item in csv_string.split(','):
        stripped_item = item.strip()
        if stripped_item:
            try:
                values.append(int(stripped_item))
            except ValueError:
                values.append(stripped_item)
    return values
if __name__ == '__main__':
    sample_string = " 10 , 25 , 30 , 45 , 50 "
    result = parse_csv_optimized(sample_string)
    print(result)