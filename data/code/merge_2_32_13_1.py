import collections
def count_elements(data):
    counter = collections.Counter()
    for item in data:
        counter[item] += 1
    return dict(counter)
if __name__ == '__main__':
    sample_data = [3, 'apple', 2.5, 'banana', 3, None, 'apple']
    result = count_elements(sample_data)
    print(result)