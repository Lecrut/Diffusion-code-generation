def find_smallest(data):
    if not data:
        return None
    smallest = data[0]
    for i in range(1, len(data)):
        if data[i] < smallest:
            smallest = data[i]
    return smallest
if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2]
    result = find_smallest(sample_list)
    print(result)