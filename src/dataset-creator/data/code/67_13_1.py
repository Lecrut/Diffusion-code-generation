import sys
def convert_temperature(value: float, from_scale: str) -> tuple[float, str]:
    if from_scale == 'C':
        return (value * 9 / 5 + 32, 'F')
    elif from_scale == 'F':
        return ((value - 32) * 5 / 9, 'C')
    else:
        raise ValueError(f"Unsupported scale: {from_scale}")
def process_dataset(raw_data: list[dict]) -> dict[str, float]:
    result = {}
    for item in raw_data:
        value, new_scale = convert_temperature(item['value'], item.get('scale', 'C'))
        if new_scale not in result or abs(result[new_scale] - value) < 0.01:
            result[new_scale] = round(value, 2)
    return result
if __name__ == '__main__':
    raw_data = [
        {'value': 37.5, 'scale': 'C'},
        {'value': 98.6, 'scale': 'F'},
        {'value': -40, 'scale': 'C'},
        {'value': -40, 'scale': 'F'}
    ]
    processed = process_dataset(raw_data)
    for scale in sorted(processed.keys()):
        print(f"{scale}: {processed[scale]}")