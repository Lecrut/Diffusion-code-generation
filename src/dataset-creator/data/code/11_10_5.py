from typing import List, Any
def check_equal_values(values: List[Any]) -> bool:
    if not values:
        return True
    unique_elements = set()
    for value in values:
        try:
            hashable_value = value
        except TypeError:
            return False
        unique_elements.add(hashable_value)
    return len(unique_elements) == 1
if __name__ == '__main__':
    sample_list = [5, 3, 'a', 5]
    result = check_equal_values(sample_list)