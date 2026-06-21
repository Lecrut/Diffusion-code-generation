def find_max_element(data):
    if not data:
        raise ValueError("The list cannot be empty")
    return max(data)

if __name__ == '__main__':
    sample_list = [15, 8, 42, 3, 99, 21]
    largest = find_max_element(sample_list)
    print(largest)