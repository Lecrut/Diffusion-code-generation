import json
def process_data(records):
    aggregated = {}
    preserved_records = []
    for record in records:
        item_id = record['id']
        value = record['value']
        metadata = record.get('metadata', {})
        if 'category' not in metadata or metadata['category'] is None:
            category = 'uncategorized'
        else:
            category = metadata['category']
        preserved_records.append({
            'id': item_id,
            'value': value,
            'metadata': metadata
        })
        if category not in aggregated:
            aggregated[category] = {'count': 0, 'total_value': 0}
        aggregated[category]['count'] += 1
        aggregated[category]['total_value'] += value
    return {
        'aggregated_data': aggregated,
        'preserved_records': preserved_records
    }
if __name__ == '__main__':
    sample_data = [
        {'id': 1, 'value': 100, 'metadata': {'category': 'electronics', 'brand': 'A'}},
        {'id': 2, 'value': 50, 'metadata': {'category': 'clothing', 'size': 'M'}},
        {'id': 3, 'value': 75, 'metadata': {'category': 'electronics', 'brand': 'B'}},
        {'id': 4, 'value': 200, 'metadata': {'category': None}},
    ]
    result = process_data(sample_data)
    print("Aggregated Data:")
    for cat, stats in result['aggregated_data'].items():
        print(f"Category: {cat} - Count: {stats['count']}, Total Value: {stats['total_value']}")
    print("\nPreserved Records:")
    for rec in result['preserved_records']:
        print(json.dumps(rec, indent=2))