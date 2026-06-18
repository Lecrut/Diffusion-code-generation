import collections
def count_elements(collection):
    return dict(collections.Counter(collection))
if __name__ == '__main__':
    data = [1, 2, 'apple', 3, 'banana', 4, 'apple']
    result = count_elements(data)
    print(result)