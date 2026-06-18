from collections import Counter
def count_elements(iterable):
    return dict(Counter(iterable))
if __name__ == '__main__':
    sample_data = ['apple', 'banana', 'apple', 'orange', 'banana']
    result = count_elements(sample_data)
    print(result)