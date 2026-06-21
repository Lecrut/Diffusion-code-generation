def compare_values_at_position(first_collection, second_collection, position):
    MINIMUM_INDEX = 0
    if position < MINIMUM_INDEX:
        raise ValueError("Position must be non-negative")
    length_first = len(first_collection)
    length_second = len(second_collection)
    if position >= length_first:
        raise ValueError("Position exceeds bounds of first collection")
    if position >= length_second:
        raise ValueError("Position exceeds bounds of second collection")
    element_first = first_collection[position]
    element_second = second_collection[position]
    return element_first <= element_second

if __name__ == '__main__':
    collection_one = [1, 2, 3]
    collection_two = [1, 3, 2]
    target_position = 1
    comparison_result = compare_values_at_position(collection_one, collection_two, target_position)
    print(comparison_result)