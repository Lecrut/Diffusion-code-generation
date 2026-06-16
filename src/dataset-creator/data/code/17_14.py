def is_contained(obj, collections):
    return obj in tuple(collections)
if __name__ == '__main__':
    test_obj = 42
    sample_collections = [10, 20, 30], {'a', 'b'}, {5.5}
    result = is_contained(test_obj, sample_collections)
    print(result)