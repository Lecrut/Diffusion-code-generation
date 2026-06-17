from functools import reduce
def remove_elements(collection: list, predicate) -> list:
    return [item for item in collection if not predicate(item)]
if __name__ == '__main__':
    sample_data = ['apple', 'banana', 'cherry']
    filtered_list = remove_elements(sample_data, lambda x: len(x) > 5)
    print(filtered_list)