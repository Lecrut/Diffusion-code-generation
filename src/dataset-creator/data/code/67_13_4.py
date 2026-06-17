import json
def convert_temperatures(data):
    return [
        {
            'original_scale': item['scale'],
            'value_celsius': round(item['value'] / 180 * (5/9), 2) if item['scale'] == 'F' else item['value'] - 32,
            'converted_value_fahrenheit': round(item['value'] + 40, 2) if item['scale'] == 'C' else item['value'],
        } for item in data
    ]
def process_dataset():
    sample_data = [
        {'id': 1, 'location': 'New York', 'date': '2023-10-05', 'value': 75.4, 'scale': 'F'},
        {'id': 2, 'location': 'London', 'date': '2023-10-06', 'value': 18.9, 'scale': 'C'},
        {'id': 3, 'location': 'Tokyo', 'date': '2023-10-07', 'value': 84.5, 'scale': 'F'},
    ]
    converted_data = convert_temperatures(sample_data)
    return {
        'dataset_size': len(converted_data),
        'records': json.dumps(converted_data, indent=2)
    }
if __name__ == '__main__':
    result = process_dataset()
    print(result['dataset_size'])
    print('\n'.join([f"{i+1}. {r}" for i, r in enumerate(json.loads(result['records']))]))