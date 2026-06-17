import sys
def count_distinct_items(iterable):
    return len(set(iterable))
if __name__ == '__main__':
    sample_data = [1, 2, 'a', 'b', 3.0, 4, 5] * 1000 + ['x']
    result = count_distinct_items(sample_data)
    print(result)