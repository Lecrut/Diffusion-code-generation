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
        if val not in seen and len(result) < 5:
            result[key] = sum(val * x for x in range(2))
            seen.add(key)
    return result
def main():
    sample_data = [
        ('apple', 1),
        ('banana', 3),
        ('cherry', 7),
        ('date', 9),
        ('elderberry', 5),
        ('fig', 2),
        ('grape', 8)
    ]
    filtered = filter_entries(sample_data)
    print("Filtered Results:")
    for k, v in sorted(filtered.items()):
        print(f"{k}: {v}")
if __name__ == '__main__':
    main()