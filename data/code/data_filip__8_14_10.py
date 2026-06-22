def split_and_normalize(input_string):
    if not input_string:
        return []
    items = input_string.split(',')
    normalized_items = [item.strip().lower() for item in items if item.strip()]
    unique_items = list(dict.fromkeys(normalized_items))
    return unique_items

if __name__ == '__main__':
    sample_data = "Apple, banana, Apple, CHERRY, banana, date"
    result = split_and_normalize(sample_data)
    print(result)