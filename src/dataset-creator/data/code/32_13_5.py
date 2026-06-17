from collections import Counter
def count_elements_in_set(collection):
    return dict(Counter(collection))
if __name__ == '__main__':
    sample_data = [1, 2, 'a', 3, 'b', 4, 'c', 5, 'd'] + ['e' * 2]
    result = count_elements_in_set(sample_data)
    print(result)