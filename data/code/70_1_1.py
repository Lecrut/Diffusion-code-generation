def check_first_and_last(data):
    if not data:
        return None, None
    first = data[0]
    last = data[-1]
    return first, last
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    first_val, last_val = check_first_and_last(sample_list)
    print(f"First: {first_val}, Last: {last_val}")
    sample_list_two = [5]
    first_val_two, last_val_two = check_first_and_last(sample_list_two)
    print(f"First: {first_val_two}, Last: {last_val_two}")
    sample_list_three = []
    first_val_three, last_val_three = check_first_and_last(sample_list_three)
    print(f"First: {first_val_three}, Last: {last_val_three}")
    sample_list_four = [100]
    first_val_four, last_val_four = check_first_and_last(sample_list_four)
    print(f"First: {first_val_four}, Last: {last_val_four}")