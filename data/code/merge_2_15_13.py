import sys
def sort_integers(data):
    return sorted(data)
def sort_floats(data):
    return sorted(data, reverse=False)
if __name__ == '__main__':
    sample_integers = [45, 23, -10, 67, 89, 12]
    sample_floats = [3.14, 2.71, 1.41, 0.57, 9.99]
    print("Sorted Integers:", sort_integers(sample_integers))
    print("Sorted Floats:", sort_floats(sample_floats))