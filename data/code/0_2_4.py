def process_list(initial_list: list[int], new_value_str: str) -> list[int]:
    result = list(initial_list)
    try:
        new_value = int(new_value_str)
        result.append(new_value)
    except ValueError:
        result = list(initial_list)
        print("Error: Invalid input. Must be an integer.")