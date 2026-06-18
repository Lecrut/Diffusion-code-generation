import json
def process_data(data):
    aggregated = {}
    preserved_records = []
    for item in data:
        record_id = item['id']
        category = item.get('category', 'unknown')
        if category not in aggregated:
            aggregated[category] = {'count': 0, 'total_value': 0}
        agg = aggregated[category]
        agg['count'] += 1
        agg['total_value'] += item['value']
        preserved_records.append({
            'id': record_id,
            'value': item['value'],
            'metadata': item.get('metadata', {})
        })
    return aggregated, preserved_records
if __name__ == '__main__':
    sample_data = [
        {'id': 1, 'value': 100, 'category': 'electronics', 'metadata': {'brand': 'A'}},
        {'id': 2, 'value': 50, 'category': 'clothing', 'metadata': {'size': 'M'}},
        {'id': 3, 'value': 75, 'category': 'electronics', 'metadata': {'model': 'X'}},
        {'id': 4, 'value': 200, 'category': 'clothing', 'metadata': {'color': 'Red'}}
    ]
    aggregation_result, records_output = process_data(sample_data)
    print("Aggregated Data:")
    for cat, stats in aggregation_result.items():
        print(f"{cat}: Count={stats['count']}, Total Value={stats['total_value']}")
    print("\nPreserved Records:")
    json.dump(records_output, open('output_records.json', 'w'), indent=2)