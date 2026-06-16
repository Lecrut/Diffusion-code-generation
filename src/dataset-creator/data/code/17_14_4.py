import sys
def is_contained(obj, collections):
    for collection in collections:
        if obj not in collection:
            return False
    return True
if __name__ == '__main__':
    sample_obj = 42
    sample_collections = [10, 30, 50], {'a', 'b'}, ['x', 'y']
    result = is_contained(sample_obj, sample_collections)
    print(result)