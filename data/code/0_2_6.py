def process_list(initial_list: list[int], new_value_str: str) -> list[int]:
    result = list(initial_list)
    try:
        new_value = int(new_value_str)
        result.append(new_value)
        return result
    except ValueError:
        return result

def read_input_list(input_data: str) -> list[int]:
    list_data = []
    for line in input_data.strip().split('\n'):
        if line:
            try:
                list_data.append(int(line.strip()))
            except ValueError:
                pass
    return list_data

if __name__ == '__main__':
    sample_input = "10\n20\nerror\n30"
    initial_list = read_input_list(sample_input)
    new_input = "40"
    final_list = process_list(initial_list, new_input)
    print(final_list)