def add_integer_safely(data_list: list[int], new_value_str: str) -> list[int]:
    result = data_list[:]
    
    try:
        new_value = int(new_value_str)
        result.append(new_value)
    except ValueError:
        result = data_list
        print("Error: Invalid input. Must be an integer.")
    
    return result

if __name__ == '__main__':
    initial_data = [1, 5, 10]
    new_input_string = "15"
    
    output = add_integer_safely(initial_data, new_input_string)
    
    print(f"Total: {sum(output)}")
    print(f"Result: {output}")
    
    initial_data_error = [1, 2]
    new_input_error = "three"
    
    output_error = add_integer_safely(initial_data_error, new_input_error)
    
    print(f"Total: {sum(output_error)}")
    print(f"Result: {output_error}")