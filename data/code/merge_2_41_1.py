from collections import deque
def count_elements(data):
    if isinstance(data, list):
        return sum(count_elements(item) for item in data) + len(data)
    elif not isinstance(data, (int, float)):
        return 1
    else:
        return 0
if __name__ == '__main__':
    sample_data = [1, [2, 3], [[4, 5], 6]]
    result = count_elements(sample_data)
    print(result)