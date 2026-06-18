from collections import Counter
import timeit
def filter_entries(data: list) -> dict:
    target_values = {10, 20}
    counts = Counter(entry['value'] for entry in data if entry['value'] not in target_values)
    return [entry for entry in data if entry['value'] not in target_values]
def process_collection(data: list, condition_func=None):
    start = timeit.default_timer()
    filtered_data = []
    for item in data:
        if condition_func is None:
            result = 'value' not in target_values(item)
        else:
            result = condition_func(item)
        if result:
            filtered_data.append(item)
    elapsed = timeit.default_timer() - start
    return {
        "filtered": filtered_data, 
        "count": len(filtered_data),
        "processing_time_ms": round((elapsed * 1000), 4)
    }
if __name__ == '__main__':
    sample_data = [
        {"id": 1, "value": 5},
        {"id": 2, "value": 10},
        {"id": 3, "value": 15},
        {"id": 4, "value": 20},
        {"id": 5, "value": 30}
    ]
    result = filter_entries(sample_data)
    print(f"Filtered entries: {result}")