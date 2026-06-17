def find_middle_index(data):
    if not data:
        return None
    length = len(data)
    middle_position = (length - 1) // 2
    return middle_position
if __name__ == '__main__':
    sample_list = [0, 1, 2, 3, 4]
    result_index = find_middle_index(sample_list)
    if result_index is not None:
        print(f"Middle index of {sample_list}: {result_index}")
    else:
        print("Input list was empty.")