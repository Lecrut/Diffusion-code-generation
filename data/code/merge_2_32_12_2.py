import sys
def count_distinct_items(iterable):
    return len(set(iterable))
if __name__ == '__main__':
    sample_data = [1, 2, 'a', 3.0, True, False] * 1000 + list(range(5000))
    result = count_distinct_items(sample_data)
    print(result)