import math

def get_median(data):
    if not data:
        raise ValueError("List must not be empty")
    sorted_data = sorted(data)
    length = len(sorted_data)
    mid = length // 2
    if length % 2 == 0:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2
    return sorted_data[mid]

if __name__ == '__main__':
    sample_list = [7, 1, 3, 5, 9]
    result = get_median(sample_list)
    print(result)