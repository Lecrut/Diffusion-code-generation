def find_largest(data):
    if not data:
        return None
    largest = max(data)
    return largest

if __name__ == '__main__':
    sample_list = [15, 8, 22, 3, 45, 10]
    result = find_largest(sample_list)
    print(result)