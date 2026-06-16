from collections import Counter
def count_items(collection):
    return dict(Counter(collection))
if __name__ == '__main__':
    sample_data = [10, 20, 30, 20, 40, 50, 20]
    result = count_items(sample_data)
    print(result)