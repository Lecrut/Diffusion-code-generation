import sys
def convert_temperature(value: float, from_scale: str) -> dict:
    if from_scale not in ['C', 'F']:
        raise ValueError("Unsupported scale")
    celsius = value
    if from_scale == 'F':
        celsius = (value - 32) * 5 / 9
    return {
        'original_value': value,
        'from_scale': from_scale,
        'celsius': round(celsius, 2),
        'fahrenheit': round(value + ((round(celsius, 2) - 32) * 9 / 5), 2) if celsius != value else round((value - 32) * 9 / 5 + 32, 2)
    }
def process_dataset(raw_data: list) -> dict:
    processed_records = []
    for record in raw_data:
        try:
            converted_info = convert_temperature(record['temperature'], record.get('scale', 'C'))
            processed_records.append(converted_info)
        except Exception as e:
            print(f"Error processing {record}: {e}", file=sys.stderr)
    return {'records': processed_records, 'total_processed': len(processed_records)}
if __name__ == '__main__':
    sample_data = [
        {'temperature': 25.0, 'scale': 'C'},
        {'temperature': 77.0, 'scale': 'F'},
        {'temperature': -4.0, 'scale': 'C'},
        {'temperature': 31.6, 'scale': 'F'}
    ]
    result = process_dataset(sample_data)
    print(result['records'])