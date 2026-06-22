def split_and_clean_string(input_string: str) -> list:
    items = input_string.split(',')
    cleaned_items = [item.strip() for item in items if item.strip()]
    return cleaned_items

if __name__ == '__main__':
    test_string = "  apple, , banana, , ,  cherry , date "
    result = split_and_clean_string(test_string)
    print(result)