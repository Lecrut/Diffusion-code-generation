from collections import deque
def count_elements(data):
    if isinstance(data, list):
        return sum(count_elements(item) for item in data) + len(data)
    else:
        return 1
if __name__ == '__main__':
    sample_data = [1, [2, 3], [[4, 5], 6]]
    total_count = count_elements(sample_data)
    print(total_count)