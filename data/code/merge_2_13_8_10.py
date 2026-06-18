import sys
def track_running_maximum(values):
    if not values:
        return None
    running_max = float('-inf')
    for value in values:
        if value > running_max:
            running_max = value
    return running_max
if __name__ == '__main__':
    sample_data = [3, 7, 2, 9, 4, -5, 10]
    result = track_running_maximum(sample_data)
    print(result)