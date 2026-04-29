def process_list(initial_list: list[int], new_value_str: str) -> list[int]:
    result = list(initial_list)
    try:
        new_value = int(new_value_str)
        result.append(new_value)
    except ValueError:
        result = initial_list
        print("Error: Invalid input. Must be an integer.")
    return result

def read_input_list(input_data: str) -> list[int]:
    list_data = []
    for line in input_data.strip().split():
        if line:
            try:
                list_data.append(int(line))
            except ValueError:
                print("Error: Non-integer found in input list.")
                return []
    return list_data

if __name__ == '__main__':
    input_data = "10 20 30"
    new_input = "40"
    
    initial_list = read_input_list(input_data)
    
    if initial_list:
        final_list = process_list(initial_list, new_input)
        print(final_list)
    else:
        print("List processing failed.")