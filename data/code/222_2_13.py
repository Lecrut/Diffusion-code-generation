import math

def find_min(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    minimum = float('inf')
    for item in data:
        if not math.isnan(item) and item < minimum:
            minimum = item
    return minimum

if __name__ == '__main__':
    sample_list = [45, 12, 89, 3, 56, float('nan'), 7]
    result = find_min(sample_list)
    print(result)