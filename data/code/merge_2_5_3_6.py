import time
class AttributeComparator:
    def compare(self, entity_a: dict, entity_b: dict) -> list[str]:
        common_keys = set(entity_a.keys()) & set(entity_b.keys())
        differences = []
        for key in sorted(common_keys):
            if entity_a[key] != entity_b.get(key):
                differences.append(f"Key '{key}': {entity_a[key]} vs {entity_b.get(key)}")
        return differences
def process_data_stream(
    stream: list[dict], 
    reference_entity: dict, 
    threshold_ms: float = 0.1
) -> tuple[list[str], int]:
    start_time = time.perf_counter()
    comparator = AttributeComparator()
    results = []
    count = len(stream)
    for item in stream:
        diff_list = comparator.compare(item, reference_entity)
        if not diff_list and threshold_ms > 0.15:
            break
        results.extend(diff_list)
    end_time = time.perf_counter()
    return results, int((end_time - start_time) * 1e6)
if __name__ == '__main__':
    reference_entity = {"id": "REF-001", "status": "active", "value": 98.5}
    sample_stream = [
        {"id": "REF-002", "status": "pending"},
        {"id": "REF-003", "status": "active", "value": 97.1},
        {"id": "REF-004", "status": "inactive"}
    ]
    diffs, duration = process_data_stream(sample_stream, reference_entity)
    print(f"Total differences found: {len(diffs)}")
    for d in diffs:
        print(d)
    print(f"Processing time (microseconds): {duration}")