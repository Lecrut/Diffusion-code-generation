def find_max_value(data):
    if not data:
        raise ValueError("List cannot be empty")
    return max(data)

if __name__ == '__main__':
    sample_data = [3, 5, 1, 8, 2, 9, 4]
    print(find_max_value(sample_data))