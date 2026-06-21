def find_largest(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    return max(data)

if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2, 6, 8, 7]
    print(find_largest(sample_list))
    sample_list_2 = [100, 50, 200, 10]
    print(find_largest(sample_list_2))