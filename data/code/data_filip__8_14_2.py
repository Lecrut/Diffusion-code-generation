def process_string_data(raw_data):
    items = raw_data.split(',')
    normalized_items = [item.strip().lower() for item in items]
    unique_items = list(dict.fromkeys(normalized_items))
    return unique_items

if __name__ == '__main__':
    sample_input = "Apple, BANANA, apple, Cherry, Date, banana, APPLE"
    result = process_string_data(sample_input)
    print(result)