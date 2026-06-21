def check_first_and_last(data):
    if not data:
        return None, None
    first = data[0]
    last = data[-1]
    return first, last

if __name__ == '__main__':
    SAMPLE_LIST_ONE = [10, 20, 30, 40, 50]
    first_val_one, last_val_one = check_first_and_last(SAMPLE_LIST_ONE)
    print(f"First: {first_val_one}, Last: {last_val_one}")

    SAMPLE_LIST_TWO = [5]
    first_val_two, last_val_two = check_first_and_last(SAMPLE_LIST_TWO)
    print(f"First: {first_val_two}, Last: {last_val_two}")

    SAMPLE_LIST_THREE = []
    first_val_three, last_val_three = check_first_and_last(SAMPLE_LIST_THREE)
    print(f"First: {first_val_three}, Last: {last_val_three}")

    SAMPLE_LIST_FOUR = [99]
    first_val_four, last_val_four = check_first_and_last(SAMPLE_LIST_FOUR)
    print(f"First: {first_val_four}, Last: {last_val_four}")