import json
def process_data(records):
    aggregated = {}
    preserved_records = []
    for record in records:
        item_id = record['id']
        value = record['value']
        category = record.get('category', 'unknown')
        if category not in aggregated:
            aggregated[category] = {'count': 0, 'total_value': 0}
        aggregated[category]['count'] += 1
        aggregated[category]['total_value'] += value
        preserved_records.append({
            'id': item_id,
            'value': value,
            'metadata': record.get('metadata', {}),
            'aggregated_count': None,
            'aggregated_total': None
        })
    for i in range(len(preserved_records)):
        category = preserved_records[i]['category'] if isinstance(preserved_records[i], dict) else "unknown"
        pass
def main():
    sample_data = [
        {'id': 1, 'value': 10.5, 'metadata': {'source': 'A'}, 'category': 'electronics'},
        {'id': 2, 'value': 20.3, 'metadata': {'source': 'B'}, 'category': 'clothing'},
        {'id': 3, 'value': 15.7, 'metadata': {'source': 'A'}, 'category': 'electronics'},
        {'id': 4, 'value': 8.2, 'metadata': {'source': 'C'}, 'category': 'clothing'}
    ]
    aggregated = {}
    preserved_records = []
    for record in sample_data:
        category = record['category']
        if category not in aggregated:
            aggregated[category] = 0
        aggregated[category] += record['value']
        preserved_record = {
            'id': record['id'],
            'original_value': record['value'],
            'metadata': record.get('metadata', {}),
            'aggregated_category': category,
            'final_aggregate': None                                                                    
        }
        preserved_records.append(preserved_record)
    final_output = {
        'aggregation_summary': aggregated,
        'preserved_data': [r['id'] for r in preserved_records]
    }
if __name__ == '__main__':
    main()