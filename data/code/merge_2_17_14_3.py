from collections import Counter
def contains_in_collection(obj, collection):
    return obj in collection
if __name__ == '__main__':
    sample_list = [10, 20, 30]
    sample_set = {40, 50}
    sample_tuple = (60,)
    test_objects = [10, 'hello', None]
    results = []
    for obj in test_objects:
        is_in_list = contains_in_collection(obj, sample_list)
        is_in_set = contains_in_collection(obj, sample_set)
        is_in_tuple = contains_in_collection(obj, sample_tuple)
        if isinstance(sample_list, list):
            results.append((obj, 'list', is_in_list))
        elif isinstance(sample_set, set):
            results.append((obj, 'set', is_in_set))
        else:
            results.append((obj, 'tuple', is_in_tuple))
    for obj, collection_type, found in results:
        print(f"Object {repr(obj)} {'found' if found else 'not found'} in {collection_type}")