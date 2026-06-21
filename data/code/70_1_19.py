def validate_input(data):
    if not isinstance(data, list):
        raise ValueError("Input must be a list")
    if len(data) == 0:
        return None, None

def check_first_and_last(data):
    first, last = validate_input(data)
    if first is None and last is None:
        return None, None
    return data[0], data[-1]

if __name__ == '__main__':
    sample_list = [15, 25, 35, 45, 55]
    first_val, last_val = check_first_and_last(sample_list)
    print(f"First: {first_val}, Last: {last_val}")
    
    sample_list_two = [7]
    first_val_two, last_val_two = check_first_and_last(sample_list_two)
    print(f"First: {first_val_two}, Last: {last_val_two}")
    
    sample_list_three = []
    first_val_three, last_val_three = check_first_and_last(sample_list_three)
    print(f"First: {first_val_three}, Last: {last_val_three}")
    
    sample_list_four = [105]
    first_val_four, last_val_four = check_first_and_last(sample_list_four)
    print(f"First: {first_val_four}, Last: {last_val_four}")