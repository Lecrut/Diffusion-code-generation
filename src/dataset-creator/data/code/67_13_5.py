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
            val = float(record['temperature'])
            scale = str(record.get('scale', 'C'))
            if not isinstance(val, (int, float)):
                continue
            converted_info = convert_temperature(val, scale)
            processed_records.append(converted_info)
        except Exception:
            pass
    return {
        'total_processed': len(processed_records),
        'records': processed_records
    }
if __name__ == '__main__':
    sample_data = [
        {'temperature': 25, 'scale': 'C'},
        {'temperature': 77.0, 'scale': 'F'},
        {'temperature': -4, 'scale': 'C'},
        {'temperature': 318.67, 'scale': 'F'}
    ]
    result = process_dataset(sample_data)
    print(f"Total records processed: {result['total_processed']}")
    for r in result['records']:
        print(r)