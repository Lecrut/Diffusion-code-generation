import json
def process_data(data):
    aggregated = {}
    preserved_records = []
    for item in data:
        category = item.get('category', 'unknown')
        if category not in aggregated:
            aggregated[category] = {'count': 0, 'sum': 0}
        value = float(item['value'])
        metadata = item.get('metadata', {})
        aggregated[category]['count'] += 1
        aggregated[category]['sum'] += value
        preserved_records.append({
            'id': item['id'],
            'value': value,
            'metadata': metadata
        })
    return {k: v for k, v in sorted(aggregated.items())}, preserved_records
if __name__ == '__main__':
    sample_data = [
        {'id': 101, 'category': 'electronics', 'value': 250.00, 'metadata': {'brand': 'A'}},
        {'id': 102, 'category': 'clothing', 'value': 45.99, 'metadata': {'size': 'M'}},
        {'id': 103, 'category': 'electronics', 'value': 120.50, 'metadata': {'brand': 'B'}},
        {'id': 104, 'category': 'clothing', 'value': 89.00, 'metadata': {'size': 'L'}}
    ]
    aggregated_stats, records = process_data(sample_data)
    print("Aggregated Data:")
    for cat, stats in aggregated_stats.items():
        print(f"{cat}: Count={stats['count']}, Sum=${stats['sum']}")
    print("\nPreserved Records:")
    for rec in records:
        print(json.dumps(rec))