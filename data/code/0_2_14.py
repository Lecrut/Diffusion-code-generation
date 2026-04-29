def process_list(initial_list: list[int], new_value_str: str) -> tuple[list[int], bool]:
    result = initial_list[:]
    try:
        new_value = int(new_value_str)
        result.append(new_value)
        return result, True
    except ValueError:
        return result, False

def main_processor(data: list[int], input_str: str):
    final_list, success = process_list(data, input_str)
    if success:
        print(final_list)
    else:
        print("Error: Invalid input provided.")

if __name__ == '__main__':
    initial_data = [1, 5, 10]
    user_input = "15"
    main_processor(initial_data, user_input)

    initial_data_2 = [20, 30]
    user_input_2 = "hello"
    main_processor(initial_data_2, user_input_2)