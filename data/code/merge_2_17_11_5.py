def contains_target(iterable: any, target) -> bool:
    try:
        for item in iterable:
            if item == target:
                return True
        return False
    except TypeError as e:
        raise ValueError(f"Input must be an iterable. Error: {e}")
if __name__ == '__main__':
    sample_list = [1, 2, 3]
    sample_tuple = (4, 5, 6)
    sample_set = {'a', 'b'}
    target_1 = 3
    target_2 = 7
    print(contains_target(sample_list, target_1))       
    print(contains_target(sample_list, target_2))        
    print(contains_target(sample_tuple, target_1))        
    print(contains_target(sample_set, 'a'))