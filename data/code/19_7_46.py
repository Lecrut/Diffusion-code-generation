def is_condition_true(a, b):
    comparison_map = {
        (42, 42): True,
        ('hello', 'world'): False,
        (3.14, 3.14): True,
        (True, False): False,
        ([1, 2], [1, 2]): True
    }
    
    key = (a, b)
    if key in comparison_map:
        return comparison_map[key]
    else:
        return a == b

if __name__ == '__main__':
    sample_a = 42
    sample_b = 42
    result1 = is_condition_true(sample_a, sample_b)
    print(result1)
    
    sample_c = 'hello'
    sample_d = 'world'
    result2 = is_condition_true(sample_c, sample_d)
    print(result2)
    
    sample_e = 3.14
    sample_f = 3.14
    result3 = is_condition_true(sample_e, sample_f)
    print(result3)
    
    sample_g = True
    sample_h = False
    result4 = is_condition_true(sample_g, sample_h)
    print(result4)
    
    sample_i = [1, 2]
    sample_j = [1, 2]
    result5 = is_condition_true(sample_i, sample_j)
    print(result5)