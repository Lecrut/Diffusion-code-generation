def process_list(initial_list: list[int], new_value_str: str) -> tuple[list[int] | None, str]:
    result = initial_list[:]
    
    try:
        new_value = int(new_value_str)
        result.append(new_value)
        return result, "success"
    except ValueError:
        return None, "error: invalid input"

def read_input_list(input_data: str) -> list[int]:
    list_data = []
    for line in input_data.strip().split('\n'):
        if line:
            try:
                list_data.append(int(line.strip()))
            except ValueError:
                return []
    return list_data

if __name__ == '__main__':
    input_data = "10\n20\n30"
    
    initial_list = read_input_list(input_data)
    
    if not initial_list:
        print("empty")
    else:
        new_input = "40"
        final_list, status = process_list(initial_list, new_input)
        
        if final_list is not None:
            print(f"result: {final_list}")
            print(f"status: {status}")
        else:
            print(f"error: {status}")
            
    new_input_error = "forty"
    final_list_error, status_error = process_list(initial_list, new_input_error)
    
    if final_list_error is not None:
        print(f"result: {final_list_error}")
        print(f"status: {status_error}")
    else:
        print(f"error: {status_error}")