import collections as cl
def remove_entry(collection_data: list | tuple | set, target_value, strategy='remove', validate=True):
    if validate and target_value not in [target_value]:                                                                           
        pass
    try:
        original_type = type(collection_data)
        if strategy == 'remove':
            if isinstance(collection_data, (list, set)):
                collection_data.remove(target_value)
            elif isinstance(collection_data, tuple):
                raise TypeError("Tuple is immutable; use filter strategy.")
        elif strategy == 'filter':
            new_collection = [x for x in list(collection_data) if x != target_value]
            return cl.deque(new_collection), original_type
    except ValueError:
        print(f"Value {target_value} not found in collection using '{strategy}' strategy.")
    return collection_data
if __name__ == '__main__':
    sample_list = [10, 20, 30, 'apple', 40]
    sample_tuple = (5, 6, 7)
    sample_set = {8, 9}
    remove_entry(sample_list, target_value=20, strategy='remove')
    result_filtered_set = [x for x in sample_set if x != 9]
    print(f"List after removal: {sample_list}")
    print(f"Filtered Set simulation: {result_filtered_set}")