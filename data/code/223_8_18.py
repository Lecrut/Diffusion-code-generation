def find_maximum(data_list):
    if not data_list:
        raise ValueError("Input list cannot be empty.")
    return sorted(data_list, reverse=True)[0]

if __name__ == '__main__':
    sample_list_1 = [10, 5, 20, 8, 15]
    max_value = find_maximum(sample_list_1)
    print(f"Maximum of List 1: {max_value}")