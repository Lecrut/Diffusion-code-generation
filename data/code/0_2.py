def add_integer_to_list(input_list: list[int], new_value: str) -> list[int]:
    result = input_list[:]
    try:
        new_int = int(new_value)
        result.append(new_int)
    except ValueError:
        pass
    return result

def process_input_stream(input_data: str) -> list[int]:
    list_data = []
    for line in input_data.strip().split('\n'):
        if line:
            try:
                list_data.append(int(line.strip()))
            except ValueError:
                pass
    return list_data

if __name__ == '__main__':
    initial_data_str = "10\n20\nerror\n30"
    new_input_str = "40"

    initial_list = process_input_stream(initial_data_str)
    
    final_list = add_integer_to_list(initial_list, new_input_str)

    print(final_list)