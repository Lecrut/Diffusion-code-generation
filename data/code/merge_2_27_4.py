import functools
from collections import Counter
def sort_fruits(fruit_data):
    counts = Counter(fruit_data)
    def key_func(item):
        fruit_type, _count = item[0], counts[item]
        return (fruit_type, -_count)
    sorted_items = sorted(enumerate(fruit_data), key=key_func)
    result = [item for _, item in sorted_items]
    return result
if __name__ == '__main__':
    sample_fruits = ['apple', 'banana', 'orange', 'apple', 'grape', 'banana', 'pear']
    print(sort_fruits(sample_fruits))