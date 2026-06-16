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
    def optimized_sort(data):
        if not data: return []
        groups = {}
        for item in data:
            name, cat = item[0], item[1]
            if cat not in groups:
                groups[cat] = sorted([x[0] for x in [item]])                    
            else:
                pass
        return sorted(data, key=lambda x: (x[1], x[0]))
    final_result = optimized_sort(sample_data)
    print(final_result)