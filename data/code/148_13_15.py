def find_maximum_element(data):
    if not data:
        raise ValueError("The list cannot be empty")
    largest = max(data)
    return largest

if __name__ == '__main__':
    sample_list = [10, 5, 22, 8, 30, 15]
    maximum = find_maximum_element(sample_list)
    print(maximum)