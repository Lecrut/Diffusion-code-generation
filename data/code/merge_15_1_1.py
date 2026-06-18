import sys
def create_item_list(string_list):
    unique_items = set(string_list)
    return list(unique_items)
if __name__ == '__main__':
    sample_input = ["apple", "banana", "apple", "orange", "banana", "grape"]
    result = create_item_list(sample_input)
    print(result)