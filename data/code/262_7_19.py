def find_min_max(data):
    if not isinstance(data, list) or not all((isinstance(item, (int, list)) for item in data)):
        raise ValueError('Input must be a nested list of integers')
    minimum = float('inf')
    maximum = float('-inf')

    def traverse(sublist):
        nonlocal minimum, maximum
        for item in sublist:
            if isinstance(item, list):
                traverse(item)
            else:
                if item < minimum:
                    minimum = item
                if item > maximum:
                    maximum = item
    traverse(data)
    return (minimum if minimum != float('inf') else None, maximum if maximum != float('-inf') else None)
if __name__ == '__main__':
    sample_data = [[3, 1, [2]], [8], [4, [5, 9]], [1]]
    print(find_min_max(sample_data))