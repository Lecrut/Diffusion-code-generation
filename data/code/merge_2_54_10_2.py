def find_middle_index(data):
    if not data:
        return -1
    length = len(data)
    return length // 2
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    middle_index = find_middle_index(sample_list)
    if middle_index != -1:
        print(f"Middle index of {sample_list}: {middle_index}")
    else:
        empty_input = []
        result = find_middle_index(empty_input)
        print(f"Result for empty input: {result}")