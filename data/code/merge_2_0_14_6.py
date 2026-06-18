def are_equal(a: object, b: object) -> bool:
    return a == b
if __name__ == '__main__':
    sample_unhashable_list = [1, 2, 3]
    sample_hashable_tuple = (1, 2, 3)
    print(are_equal(sample_unhashable_list, sample_unhashable_list))        
    print(are_equal(sample_unhashable_list, sample_hashable_tuple))