def is_condition_true(a, b):
    comparison_map = {
        (42, 42): True,
        ('hello', 'hello'): True,
        (3.14, 3.14): True,
        (True, True): True,
        (False, False): True,
        (None, None): True
    }
    key = (a, b)
    return comparison_map.get(key, a == b)

if __name__ == '__main__':
    sample_a = 42
    sample_b = 42
    result1 = is_condition_true(sample_a, sample_b)
    print(result1)
    
    sample_c = "hello"
    sample_d = "world"
    result2 = is_condition_true(sample_c, sample_d)
    print(result2)
    
    sample_e = None
    sample_f = None
    result3 = is_condition_true(sample_e, sample_f)
    print(result3)