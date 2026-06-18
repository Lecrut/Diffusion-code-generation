from collections import Counter
def count_elements(collection):
    return dict(Counter(collection))
if __name__ == '__main__':
    sample_data = [1, 2, 'a', 3, 'b', 4, 'c'] * 5 + ['a']
    result = count_elements(sample_data)
    print(result)