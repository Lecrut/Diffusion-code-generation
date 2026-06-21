MAX_VALUE = float('-inf')

def find_largest_number(values):
    if not values:
        return None
    largest = MAX_VALUE
    for value in values:
        if value > largest:
            largest = value
    return largest

if __name__ == '__main__':
    sample_dict = {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}
    print(f"Largest number: {find_largest_number(sample_dict.values())}")