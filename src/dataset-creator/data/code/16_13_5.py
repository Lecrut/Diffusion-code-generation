from collections import Counter
def count_items(collection):
    return dict(Counter(collection))
if __name__ == '__main__':
    sample_data = [1, 2, 3, 'a', 'b', 'c']
    result = count_items(sample_data)
    print(result)