import functools
from collections import Counter
def sort_fruits(fruit_data):
    counts = Counter()
    for item in fruit_data:
        if isinstance(item, tuple) and len(item) == 2:
            name, category = item
            counts[name] += 1
    unique_types = sorted(counts.keys())
    def sort_key(x):
        return (x[0], x[1])
    result = []
    for fruit in fruit_data:
        if isinstance(fruit, tuple) and len(fruit) == 2:
            name, category = fruit
            idx = unique_types.index(name)
            count = counts[name]
            result.append((idx, count, fruit))
    return [item[2] for item in sorted(result)]
if __name__ == '__main__':
    sample_data = [('apple', 'red'), ('banana', 'yellow'), ('cherry', 'red'), 
                   ('date', 'purple'), ('elderberry', 'blue'), ('fig', 'green')]
    sorted_fruits = sort_fruits(sample_data)
    print(sorted_fruits)