import collections
def count_elements(iterable):
    counter = collections.Counter()
    for item in iterable:
        counter[item] += 1
    return dict(counter)
if __name__ == '__main__':
    sample_data = [3, 'apple', True, None, 2.5, 'banana', 'apple']
    result = count_elements(sample_data)
    print(result)