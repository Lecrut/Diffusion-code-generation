def validate_indices(first_collection, second_collection, target_position):
    if not isinstance(first_collection, (list, tuple)):
        raise ValueError("First argument must be a sequence")
    if not isinstance(second_collection, (list, tuple)):
        raise ValueError("Second argument must be a sequence")
    if not isinstance(target_position, int):
        raise ValueError("Index must be an integer")
    if target_position < 0:
        raise ValueError("Index cannot be negative")
    if target_position >= len(first_collection):
        raise ValueError("Index out of range for first collection")
    if target_position >= len(second_collection):
        raise ValueError("Index out of range for second collection")

def compare_values_at_position(first_list, second_list, position):
    validate_indices(first_list, second_list, position)
    first_value = first_list[position]
    second_value = second_list[position]
    return first_value <= second_value

if __name__ == '__main__':
    collection_one = [1, 3, 5, 7]
    collection_two = [2, 2, 6, 8]
    query_index = 2
    comparison_outcome = compare_values_at_position(collection_one, collection_two, query_index)
    print(comparison_outcome)