def check_first_and_last(data):
    if not data:
        return None, None
    first = data[0]
    last = data[-1] if len(data) > 1 else first
    return first, last

if __name__ == '__main__':
    sample_list_1 = [10, 20, 30, 40, 50]
    first_val_1, last_val_1 = check_first_and_last(sample_list_1)
    print(f"First: {first_val_1}, Last: {last_val_1}")

    sample_list_2 = [5]
    first_val_2, last_val_2 = check_first_and_last(sample_list_2)
    print(f"First: {first_val_2}, Last: {last_val_2}")

    sample_list_3 = []
    first_val_3, last_val_3 = check_first_and_last(sample_list_3)
    print(f"First: {first_val_3}, Last: {last_val_3}")

    sample_list_4 = [99, 88]
    first_val_4, last_val_4 = check_first_and_last(sample_list_4)
    print(f"First: {first_val_4}, Last: {last_val_4}")