from typing import List, Any
def check_equal_values(values: List[Any]) -> bool:
    if not values:
        return True
    first_value = values[0]
    for value in values[1:]:
        try:
            if id(value) != id(first_value):
                return False
        except TypeError:
            return False
    return True
if __name__ == '__main__':
    sample_list = [5, 5, 5]
    result = check_equal_values(sample_list)
    print(result)