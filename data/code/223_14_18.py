def find_max_value(data):
    if not data:
        raise ValueError("List cannot be empty")
    return max(data)

if __name__ == '__main__':
    sample_data = [3, 5, 1, 2, 4]
    try:
        result = find_max_value(sample_data)
        print(result)
    except ValueError as e:
        print(e)