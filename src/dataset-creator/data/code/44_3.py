import json
from collections import defaultdict
def parse_nested_structure(data):
    def aggregate(current_data):
        stats = {
            'total_items': 0,
            'sum_values': [],
            'max_value': float('-inf'),
            'min_value': float('inf')
        }
        if isinstance(current_data, list):
            for item in current_data:
                if isinstance(item, dict) and 'value' in item:
                    val = item['value']
                    stats['total_items'] += 1
                    try:
                        num_val = float(val)
                        stats['sum_values'].append(num_val)
                        if num_val > stats['max_value']:
                            stats['max_value'] = num_val
                        if num_val < stats['min_value']:
                            stats['min_value'] = num_val
                    except (ValueError, TypeError):
                        pass                                              
                elif isinstance(item, dict) and 'nested' in item:
                    nested_stats = aggregate(item['nested'])
                    stats.update(nested_stats)
        return stats
    result = aggregate(data)
    if not result['sum_values']:
        result['average'] = 0.0
        result['max_value'] = None
        result['min_value'] = None
    else:
        result['average'] = sum(result['sum_values']) / len(result['sum_values'])
    return result
if __name__ == '__main__':
    sample_data = [
        {'value': 10, 'nested': [{'value': 20}, {'value': 30}]},
        {'value': 40, 'nested': []},
        {'value': -5}
    ]
    stats = parse_nested_structure(sample_data)
    print(json.dumps(stats))