def find_extremes(nested_list):
    smallest = float('inf')
    largest = float('-inf')

    def traverse(sublist):
        nonlocal smallest, largest
        for item in sublist:
            if isinstance(item, list):
                traverse(item)
            else:
                smallest = min(smallest, item)
                largest = max(largest, item)

    traverse(nested_list)
    return smallest, largest

if __name__ == '__main__':
    sample = [[3, 5], [1, [2, 4]], 6]
    print(find_extremes(sample))