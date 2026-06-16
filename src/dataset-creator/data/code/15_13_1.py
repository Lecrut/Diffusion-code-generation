import sys
def sort_integers(data):
    return sorted(data)
def sort_floats(data):
    return sorted(data)
if __name__ == '__main__':
    sample_data = [5234109876, 1234.56, -9876543210, 0.0]
    print("Sorted Integers:", sort_integers(sample_data))
    print("Sorted Floats:", sort_floats([x for x in sample_data if isinstance(x, float)] or [float(5), float(2), float(-1)]))