def process_list(input_list: list[int], new_value_str: str) -> tuple[list[int], bool]:
    result_list = list(input_list)
    try:
        new_value = int(new_value_str)
        result_list.append(new_value)
        return result_list, True
    except ValueError:
        return result_list, False

def main():
    initial_list = [10, 20, 30]
    new_input_valid = "40"
    new_input_invalid = "error"

    result_valid, success_valid = process_list(initial_list, new_input_valid)
    print(result_valid)

    result_invalid, success_invalid = process_list(initial_list, new_input_invalid)
    print(result_invalid)

if __name__ == '__main__':
    main()