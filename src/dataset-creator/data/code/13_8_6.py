def track_running_max(values):
    if not values:
        return None
    current_max = float('-inf')
    for value in values:
        if value > current_max:
            current_max = value
    return current_max
if __name__ == '__main__':
    sample_data = [3, 7, 2, 9, -1, 5]
    result = track_running_max(sample_data)
    print(result)