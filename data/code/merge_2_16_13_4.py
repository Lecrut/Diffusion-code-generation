from collections import Counter
def count_items(items):
    return dict(Counter(items))
if __name__ == '__main__':
    sample_data = [1, 2, 'apple', 3, 'banana', 2]
    result = count_items(sample_data)
    print(result)