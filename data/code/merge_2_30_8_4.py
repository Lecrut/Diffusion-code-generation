import json
from collections import defaultdict
def process_data(records):
    aggregated = defaultdict(list)
    preserved_records = []
    for item in records:
        category = item.get('category', 'unknown')
        value = float(item['value']) if isinstance(item['value'], str) else item['value']
        agg_item = {**item, 'aggregated_value': sum([x['value'] for x in aggregated[category]])}
        aggregated[category].append(agg_item)
    return dict(aggregated), preserved_records
if __name__ == '__main__':
    sample_data = [
        {'id': 1, 'value': 10.5, 'metadata': 'A', 'category': 'electronics'},
        {'id': 2, 'value': 20.3, 'metadata': 'B', 'category': 'clothing'},
        {'id': 3, 'value': 15.7, 'metadata': 'C', 'category': 'electronics'},
    ]
    aggregated_data, preserved_items = process_data(sample_data)
    print(json.dumps(aggregated_data))