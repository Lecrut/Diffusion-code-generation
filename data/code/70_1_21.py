def check_first_and_last(data):
    if not isinstance(data, list):
        raise ValueError("Input must be a list")
    if len(data) == 0:
        return None, None
    first = data[0]
    last = data[-1]
    return first, last

if __name__ == '__main__':
    sample_list = [15, 25, 35, 45, 55]
    try:
        first_val, last_val = check_first_and_last(sample_list)
        print(f"First: {first_val}, Last: {last_val}")
    except ValueError as e:
        print(e)

    sample_list_two = [7]
    try:
        first_val_two, last_val_two = check_first_and_last(sample_list_two)
        print(f"First: {first_val_two}, Last: {last_val_two}")
    except ValueError as e:
        print(e)

    sample_list_three = []
    try:
        first_val_three, last_val_three = check_first_and_last(sample_list_three)
        print(f"First: {first_val_three}, Last: {last_val_three}")
    except ValueError as e:
        print(e)

    sample_list_four = [100]
    try:
        first_val_four, last_val_four = check_first_and_last(sample_list_four)
        print(f"First: {first_val_four}, Last: {last_val_four}")
    except ValueError as e:
        print(e)