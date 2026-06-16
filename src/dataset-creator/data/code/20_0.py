import sys
def filter_positive_values(data):
    filtered = []
    for item in data:
        try:
            if float(item) >= 0:
                filtered.append(float(item))
        except (ValueError, TypeError):
            continue
    return filtered
if __name__ == '__main__':
    sample_data = [10, -5.2, "invalid", None, 3, 7]
    result = filter_positive_values(sample_data)
    print(result)