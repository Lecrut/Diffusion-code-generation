def find_smallest_by_first_index(data):
    if not data:
        return None
    smallest = min(data, key=lambda x: x[0])
    return smallest

if __name__ == '__main__':
    sample_data = [(3, 'a'), (1, 'b'), (4, 'c'), (1, 'd'), (5, 'e')]
    result = find_smallest_by_first_index(sample_data)
    print(result)