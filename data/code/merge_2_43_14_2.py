from functools import reduce
def remove_elements(collection: list, predicate) -> list:
    return [item for item in collection if not predicate(item)]
if __name__ == '__main__':
    sample_data = ['apple', 'banana', 'cherry', 'date']
    filtered_even_length = remove_elements(sample_data, lambda x: len(x) % 2 == 0)
    print("Original:", sample_data)
    print("Filtered (odd length):", filtered_even_length)