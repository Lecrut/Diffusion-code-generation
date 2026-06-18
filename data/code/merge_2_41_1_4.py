def count_elements(data):
    total = 0
    if isinstance(data, list):
        for item in data:
            total += _count_recursive(item)
    return total
def _count_recursive(element):
    count = 1 if element is not None else 0
    if isinstance(element, (list, tuple)):
        for sub_item in element:
            count += _count_recursive(sub_item)
    return count
if __name__ == '__main__':
    sample_data = [1, [2, 3], [[4, 5], [6]], None]
    result = count_elements(sample_data)
    print(result)