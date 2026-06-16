import difflib
def are_identical(value1: object, value2: object) -> bool:
    return value1 == value2
if __name__ == '__main__':
    sample_value_1 = [10, 20, 30]
    sample_value_2 = [10, 20, 30]
    sample_value_3 = {"key": "value"}
    result_list = are_identical(sample_value_1, sample_value_2)
    result_dict = are_identical({"x": 5}, sample_value_3)
    print(f"List comparison: {result_list}")
    print(f"Dict comparison: {result_dict}")