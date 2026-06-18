import json
from collections import defaultdict
def parse_nested_structure(data):
    stats = {
        'total_items': 0,
        'category_counts': defaultdict(int),
        'value_sums': {},
        'min_values': {},
        'max_values': {}
    }
    def process_item(item):
        if isinstance(item, dict) and item.get('_type') == 'data_point':
            stats['total_items'] += 1
            category = item.get('category', 'unknown')
            stats['category_counts'][category] += 1
            value = item.get('value')
            key_id = id(item)
            if value is not None:
                try:
                    numeric_value = float(value)
                    stats['value_sums'][category] = stats['value_sums'].get(category, 0.0) + numeric_value
                    current_min = stats['min_values'].get(key_id, float('inf'))
                    if numeric_value < current_min:
                        stats['min_values'][key_id] = numeric_value
                    current_max = stats['max_values'].get(key_id, float('-inf'))
                    if numeric_value > current_max:
                        stats['max_values'][key_id] = numeric_value
                except (ValueError, TypeError):
                    pass
        elif isinstance(item, list):
            for sub_item in item:
                process_item(sub_item)
    def aggregate_by_category(category_name):
        sums = stats['value_sums'].get(category_name, 0.0)
        counts = stats['category_counts'][category_name]
        avg_value = sums / counts if counts > 0 else 0
        return {
            'count': counts,
            'sum': round(sums, 2),
            'average': round(avg_value, 4)
        }
    process_item(data)
    final_stats = {}
    for category in stats['category_counts']:
        if category != 'unknown' or stats['total_items'] > 0:
            final_stats[category] = aggregate_by_category(category)
    return {
        'summary': {
            'total_records_processed': stats['total_items'],
            'categories_found': list(stats['category_counts'].keys()),
            'aggregated_data': final_stats,
            'global_min_value': min((stats['min_values'][k] for k in stats['min_values'] if not isinstance(k, int)), default=None),
            'global_max_value': max((stats['max_values'][k] for k in stats['max_values'] if not isinstance(k, int)), default=None)
        }
    }
if __name__ == '__main__':
    sample_data = [
        {'_type': 'data_point', 'category': 'electronics', 'value': 150.5},
        [{'_type': 'nested_group', 'items': []}],
        [{'_type': 'data_point', 'category': 'clothing', 'value': 49.99}, {'_type': 'data_point', 'category': 'electronics', 'value': 200.0}],
        [1, 2, 3],                                    
        [{'_type': 'data_point', 'category': 'clothing', 'value': -5.5}]
    ]
    result = parse_nested_structure(sample_data)
    print(json.dumps(result, indent=4))