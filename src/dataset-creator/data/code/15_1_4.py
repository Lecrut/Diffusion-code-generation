import collections
def create_item_list(string_list):
    return list(set(string_list))
if __name__ == '__main__':
    sample_input = ["apple", "banana", "apple", "orange", "banana", "grape"]
    result = create_item_list(sample_input)
    print(result)