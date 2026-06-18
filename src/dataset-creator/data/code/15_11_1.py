def create_item_list(string_list):
    return [s.capitalize() for s in string_list]
if __name__ == '__main__':
    sample_input = ["apple", "banana", "cherry", "date"]
    result = create_item_list(sample_input)
    print(result)