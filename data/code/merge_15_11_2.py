def create_item_list(items):
    return [item.capitalize() for item in items]
if __name__ == '__main__':
    sample_input = ["apple", "banana", "cherry", "date"]
    result = create_item_list(sample_input)
    print(result)