def add_integer_to_list(current_list: list[int], new_value_str: str) -> tuple[list[int], bool]:
    result = current_list
    success = False
    try:
        new_value = int(new_value_str)
        result.append(new_value)
        success = True
    except ValueError:
        success = False
    return result, success

if __name__ == '__main__':
    initial_list = [10, 20, 30]
    new_input_valid = "40"
    new_input_invalid = "error"

    result_list_1, success_1 = add_integer_to_list(initial_list.copy(), new_input_valid)
    result_list_2, success_2 = add_integer_to_list(result_list_1.copy(), new_input_invalid)

    print(result_list_1)
    print(success_1)
    print(result_list_2)
    print(success_2)