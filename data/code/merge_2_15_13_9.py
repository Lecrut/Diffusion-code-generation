import sys
def sort_integers(data):
    return sorted(data)
def sort_floats(data):
    return sorted(data, key=lambda x: float(x)) if any(isinstance(i, str) for i in data) else sorted(data)
if __name__ == '__main__':
    sample_integers = [54321, 9876, -100, 42, 999]
    sample_floats = ['3.14', '2.71', '-0.5', '1e-3']
    sorted_ints = sort_integers(sample_integers)
    print(f"Sorted Integers: {sorted_ints}")
    sorted_floats = sort_floats(sample_floats)
    print(f"Sorted Floats: {sorted_floats}")