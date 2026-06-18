def find_middle_index(data):
    if not data:
        return None
    length = len(data)
    return length // 2
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    middle_index = find_middle_index(sample_list)
    if middle_index is not None:
        print(f"Middle index of {sample_list}: {middle_index}")
    else:
        print("Input list was empty.")