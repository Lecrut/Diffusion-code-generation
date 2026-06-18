from collections.abc import Iterable
def check_item_presence(data: Iterable, target) -> bool:
    try:
        if not isinstance(data, Iterable):
            raise TypeError("Input must be an iterable data structure")
        return any(item == target for item in data)
    except Exception as e:
        print(f"Error occurred while checking presence: {e}")
        return False
if __name__ == '__main__':
    sample_list = [1, 2, 3]
    sample_tuple = (4, 5, 6)
    sample_set = {7, 8}
    test_cases = [
        ("list", sample_list),
        ("tuple", sample_tuple),
        ("set", sample_set)
    ]
    for name, data in test_cases:
        result = check_item_presence(data, target=5)
        print(f"Target 5 found in {name}: {result}")
    print("\nTesting error handling for valid iterables:")
    test_list = [10]
    result_invalid_type_check = check_item_presence("not iterable", target=5)                                                                                                                 
    try:
        result = check_item_presence("string_input", target=5) 
        print(f"Result for string input (treated as iterable): {result}")
    except TypeError as te:
        print(f"Catch specific type error: {te}")