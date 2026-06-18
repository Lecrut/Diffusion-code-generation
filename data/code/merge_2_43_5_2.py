from collections import Counter
import timeit
def filter_entries(data: list) -> dict:
    seen = set()
    result = {}
    for item in data:
        if isinstance(item, tuple):
            key, val = item[0], item[1]
        else:
            continue
        if key not in seen and val > 5:
            seen.add(key)
            result[key] = sum(val * i for i in range(2))
    return result
def process_collection(items):
    filtered_items = [item for item in items if isinstance(item, tuple)]
    counts = Counter([x[1] for x in filtered_items])
    final_output = {k: v * 2 for k, v in counts.items() if v > 5}
    return final_output
if __name__ == '__main__':
    sample_data = [
        ('apple', 3),
        ('banana', 7),
        ('cherry', 4),
        ('date', 9),
        ('elderberry', 6),
        ('fig', 2)
    ]
    output1 = filter_entries(sample_data)
    output2 = process_collection(sample_data)
    print(output1)
    print(output2)