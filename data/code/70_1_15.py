def check_first_and_last(data):
    if not data:
        return None, None
    first = data[0]
    last = data[-1]
    return first, last

if __name__ == '__main__':
    SAMPLE_LIST_1 = [15, 25, 35, 45, 55]
    SAMPLE_LIST_2 = [7]
    SAMPLE_LIST_3 = []
    SAMPLE_LIST_4 = [98]

    first_val_1, last_val_1 = check_first_and_last(SAMPLE_LIST_1)
    print(f"First: {first_val_1}, Last: {last_val_1}")

    first_val_2, last_val_2 = check_first_and_last(SAMPLE_LIST_2)
    print(f"First: {first_val_2}, Last: {last_val_2}")

    first_val_3, last_val_3 = check_first_and_last(SAMPLE_LIST_3)
    print(f"First: {first_val_3}, Last: {last_val_3}")

    first_val_4, last_val_4 = check_first_and_last(SAMPLE_LIST_4)
    print(f"First: {first_val_4}, Last: {last_val_4}")