import sys

def get_minimum(values):
    if not values:
        return None
    return min(values)

if __name__ == '__main__':
    sample_data = [10, -5, 3, 8, -20, 15]
    result = get_minimum(sample_data)
    print(result)