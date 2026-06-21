def find_smallest(data):
    if not data:
        return None
    smallest = data[0]
    for element in data[1:]:
        if element < smallest[0]:
            smallest = element
    return smallest

if __name__ == '__main__':
    sample_list = [(5, 'a'), (3, 'b'), (9, 'c'), (1, 'd')]
    result = find_smallest(sample_list)
    print(result)