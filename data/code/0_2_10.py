def process_list(initial_list: list[int], new_value_str: str) -> tuple[list[int], str]:
    result = list(initial_list)
    
    try:
        new_value = int(new_value_str)
        result.append(new_value)
        output = f"Added {new_value}. New list: {result}"
    except ValueError:
        output = f"Error: Invalid input '{new_value_str}'. Input must be an integer."
        
    return result, output

if __name__ == '__main__':
    initial_data = [10, 20, 30]
    input_value_valid = "40"
    input_value_invalid = "hello"

    result_valid, output_valid = process_list(initial_data, input_value_valid)
    print(f"Result: {result_valid}")
    print(f"Output: {output_valid}")

    result_invalid, output_invalid = process_list(initial_data, input_value_invalid)
    print(f"Result: {result_invalid}")
    print(f"Output: {output_invalid}")