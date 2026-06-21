def find_middle_element(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    return data[(len(data) - 1) // 2]

if __name__ == '__main__':
    odd_sample = [4, 8, 15, 16, 23, 42]
    even_sample = [1, 2, 3]
    print(find_middle_element(odd_sample))
    print(find_middle_element(even_sample))