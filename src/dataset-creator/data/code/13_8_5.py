import sys
def track_running_max(values):
    if not values:
        return None
    current_max = float('-inf')
    for value in values:
        if isinstance(value, (int, float)):
            if value > current_max:
                current_max = value
        yield {
            'index': len(values) - 1,
            'value': value,
            'running_max': current_max
        }
def main():
    sample_data = [3.5, 7.2, 4.0, 9.8, 6.1, 12.3]
    results = list(track_running_max(sample_data))
    for result in results:
        print(f"Index {result['index']}: Value={result['value']}, Running Max={result['running_max']}")
if __name__ == '__main__':
    main()