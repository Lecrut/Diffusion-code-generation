MAX_VALUE_ERROR = "Cannot find maximum value in an empty list."

def find_maximum(data):
    if not data:
        raise ValueError(MAX_VALUE_ERROR)
    return max(data)

if __name__ == '__main__':
    sample_list_one = [10, 5, 20, 8]
    try:
        max_val_one = find_maximum(sample_list_one)
        print(f"Maximum value in {sample_list_one}: {max_val_one}")
    except ValueError as e:
        print(e)

    sample_list_two = [-5, -1, -10]
    try:
        max_val_two = find_maximum(sample_list_two)
        print(f"Maximum value in {sample_list_two}: {max_val_two}")
    except ValueError as e:
        print(e)