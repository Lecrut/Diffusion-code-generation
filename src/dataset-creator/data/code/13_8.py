def track_running_max(values):
    if not values:
        return None
    current_max = float('-inf')
    for value in values:
        if isinstance(value, (int, float)):
            if value > current_max:
                current_max = value
    return current_max
if __name__ == '__main__':
    sample_data = [3.5, 10.2, -4.7, 8.9, 15.6]
    result = track_running_max(sample_data)
    print(result)