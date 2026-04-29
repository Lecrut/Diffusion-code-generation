def process_list(initial_list: list[int], new_value_str: str) -> list[int]:
    result = list(initial_list)
    try:
        new_value = int(new_value_str)
        result.append(new_value)
    except ValueError:
        print("Error: Invalid integer input.")
        pass
    return result

if __name__ == '__main__':
    initial_list = [1, 2, 3]
    new_input = "4"
    final_list = process_list(initial_list, new_input)
    print(final_list)

    initial_list_2 = [10, 20]
    new_input_invalid = "five"
    final_list_2 = process_list(initial_list_2, new_input_invalid)
    print(final_list_2)