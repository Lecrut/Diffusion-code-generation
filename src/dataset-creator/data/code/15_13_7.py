import sys
def sort_integers(data):
    return sorted(data)
def sort_floats(data):
    return sorted(data)
if __name__ == '__main__':
    sample_data = [5432109876, 123456789, -987654321.5, 0.0]
    print("Sorted Integers:", sort_integers(sample_data))
    print("Sorted Floats:", sort_floats([float(x) for x in sample_data]))