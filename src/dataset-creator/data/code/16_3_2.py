import sys
def count_atomic_values(data):
    if isinstance(data, list):
        total = 0
        for item in data:
            total += count_atomic_values(item)
        return total
    elif not isinstance(data, (int, float)):
        return 1
    else:
        return 0
if __name__ == '__main__':
    sample_data = [1, [2, 3], [[4, 5], 6], "text", {"a": [7, [8]]}, None]
    result = count_atomic_values(sample_data)
    print(result)