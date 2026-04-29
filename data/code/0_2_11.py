def process_list(initial_list: list[int], new_value_str: str) -> list[int]:
    result = list(initial_list)
    
    try:
        new_value = int(new_value_str)
        result.append(new_value)
    except ValueError:
        # Handle non-integer input
        pass
        
    return result

if __name__ == '__main__':
    initial_data = [10, 20, 30]
    new_input = "40"
    
    final_list = process_list(initial_data, new_input)
    
    print(final_list)