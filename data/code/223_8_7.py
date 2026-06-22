def find_maximum(data_list):
    if not data_list:
        raise ValueError("Input list cannot be empty.")
    return max(data_list)

if __name__ == '__main__':
    sample_list_1 = [10, 5, 20, 8, 15]
    print(f"List 1: {sample_list_1}")
    try:
        max1 = find_maximum(sample_list_1)
        print(f"Maximum of List 1: {max1}\n")
    except ValueError as e:
        print(e)