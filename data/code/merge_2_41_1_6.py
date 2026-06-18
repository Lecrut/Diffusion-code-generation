from collections import deque
def count_elements(data):
    if not isinstance(data, list):
        return 0
    total = len(data)
    for item in data:
        if isinstance(item, list):
            total += count_elements(item)
    return total
if __name__ == '__main__':
    sample_data = [1, [2, 3], [[4, 5], [6]], 7]
    result = count_elements(sample_data)
    print(result)