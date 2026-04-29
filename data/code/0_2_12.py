def process_list(initial_list: list[int], new_value_str: str) -> tuple[list[int], bool]:
    result = initial_list[:]
    try:
        new_value = int(new_value_str)
        result.append(new_value)
        return result, True
    except ValueError:
        return result, False

def main_processor(input_data: str) -> tuple[list[int], bool]:
    initial_list = []
    try:
        for line in input_data.strip().split():
            if line:
                initial_list.append(int(line))
    except ValueError:
        return [], False

    if not initial_list:
        return [], False

    new_value_str = input_data.split()[-1]
    
    result, success = process_list(initial_list, new_value_str)
    return result, success

if __name__ == '__main__':
    sample_input = "10 20 30 40 50"
    
    result, success = main_processor(sample_input)
    
    if success:
        print(result)
    else:
        print("Error processing input")