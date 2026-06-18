def find_middle_index(collection):
    length = len(collection)
    return (length - 1) // 2
if __name__ == '__main__':
    sample_data = [0, 1, 2, 3, 4]
    result = find_middle_index(sample_data)
    print(result)