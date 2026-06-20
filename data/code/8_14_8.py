def process_string(input_string):
    items = input_string.split(',')
    normalized_items = [item.strip().lower() for item in items if item.strip()]
    unique_items = list(dict.fromkeys(normalized_items))
    return unique_items

if __name__ == '__main__':
    sample_data = "Apple, Banana, apple, Orange, banana, Grape, apple"
    result = process_string(sample_data)
    print(result)