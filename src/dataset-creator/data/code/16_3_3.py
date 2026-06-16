import sys
def count_atomic_values(data):
    if isinstance(data, list):
        total = 0
        for item in data:
            total += count_atomic_values(item)
        return total
    else:
        return 1
if __name__ == '__main__':
    sample_data = [1, 'a', {'b': [2, 3]}, [[4], ['c']], None]
    result = count_atomic_values(sample_data)
    print(result)