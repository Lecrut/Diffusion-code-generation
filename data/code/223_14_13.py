def find_max_value(data):
    if not data:
        raise ValueError("List cannot be empty")
    return max(data)

if __name__ == '__main__':
    sample_data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(find_max_value(sample_data))