import sys
def count_distinct_items(iterable):
    return len(set(iterable))
if __name__ == '__main__':
    sample_list = [1, 2, 'a', 'b', 3, 'c'] * 5000 + list(range(10000))
    result = count_distinct_items(sample_list)
    print(result)