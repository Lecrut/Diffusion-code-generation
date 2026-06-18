def count_elements(data):
    total = 0
    if isinstance(data, list):
        for item in data:
            total += _count_recursive(item)
    return total
def _count_recursive(element):
    if isinstance(element, (list, tuple)):
        return sum(_count_recursive(i) for i in element)
    else:
        return 1
if __name__ == '__main__':
    sample_data = [1, [2, 3], [[4, 5], 6]]
    result = count_elements(sample_data)
    print(result)