from collections import Counter
def count_items(collection):
    return dict(Counter(collection))
if __name__ == '__main__':
    sample_data = ['apple', 'banana', 'apple', 'orange', 'banana']
    result = count_items(sample_data)
    print(result)