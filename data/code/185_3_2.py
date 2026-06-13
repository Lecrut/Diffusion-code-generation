def parse_csv_optimized(csv_string):
    result = []
    for item in csv_string.split(','):
        stripped_item = item.strip()
        if stripped_item:
            try:
                result.append(int(stripped_item))
            except ValueError:
                result.append(stripped_item)
    return result
if __name__ == '__main__':
    sample_string = " 10 , 25 , 30 , 45 , 50 "
    parsed_data = parse_csv_optimized(sample_string)
    print(parsed_data)