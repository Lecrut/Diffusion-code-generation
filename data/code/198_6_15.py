def find_smallest(data):
    if not data:
        return None
    smallest = min(data)
    return smallest

if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2]
    result = find_smallest(sample_list)
    print(result)