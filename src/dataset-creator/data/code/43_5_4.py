from collections import Counter, defaultdict, deque
import timeit
def filter_unique_items(items: list) -> set:
    seen = set()
    filtered = []
    for item in items:
        if item not in seen:
            seen.add(item)
            filtered.append(item)
    return set(filtered)
def filter_by_condition(data: list, condition_fn) -> list:
    return [item for item in data if condition_fn(item)]
def group_and_filter_counts(items: Counter):
    filtered_items = {k: v for k, v in items.items() if v > 1}
    sorted_filtered = dict(sorted(filtered_items.items(), key=lambda x: -x[1]))
    return sorted_filtered
def process_stream(items: deque):
    processed = []
    for item in items:
        if isinstance(item, int) and 0 < item <= 100:
            processed.append(f"Processed {item}")
    return processed
if __name__ == '__main__':
    sample_data = [3, 5, 'apple', 2, 'banana', 3, 'cherry']
    unique_items = filter_unique_items(sample_data)
    filtered_numbers = filter_by_condition([i for i in range(10)], lambda x: x % 2 == 0)
    counts = Counter(sample_data * 5)
    rare_counts = group_and_filter_counts(counts)
    stream_items = deque(range(2, 12))
    processed_stream = process_stream(stream_items)
    print(f"Unique items: {unique_items}")
    print(f"Even numbers: {filtered_numbers}")
    print(f"Rare counts (>1): {rare_counts}")
    print(f"Processed stream: {processed_stream}")