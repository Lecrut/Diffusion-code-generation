from typing import List, Any
def check_equal_values(values: List[Any]) -> bool:
    try:
        first_value = values[0]
        return all(value == first_value for value in values)
    except IndexError:
        return True
if __name__ == '__main__':
    sample_list_1 = [5, 5, 5, 5]
    sample_list_2 = [3, 7, 9, 3]
    result_1 = check_equal_values(sample_list_1)
    result_2 = check_equal_values(sample_list_2)
    print(f"List {sample_list_1} has equal values: {result_1}")
    print(f"List {sample_list_2} has equal values: {result_2}")