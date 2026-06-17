from collections import Counter
import timeit
def filter_entries(data: list) -> dict:
    counts = Counter()
    for item in data:
        if isinstance(item, tuple):
            key, val = item[0], item[1]
        else:
            continue
        counts[key] += 1
    filtered = {k: v for k, v in counts.items() if v > 2}
    return filtered
def main():
    sample_data = [
        ('apple', 'red'),
        ('banana', 'yellow'),
        ('cherry', 'red'),
        ('date', 'purple'),
        ('elderberry', 'blue'),
        ('fig', 'green'),
        ('grape', 'purple'),
    ]
    result = filter_entries(sample_data)
    print(result)
if __name__ == '__main__':
    main()