def get_first_element(sequence):
    if not sequence:
        return None
    try:
        return next(iter(sequence))
    except (TypeError, StopIteration):
        return None

if __name__ == '__main__':
    sample_list = [25, 26, 27]
    sample_tuple = (28, 29, 30)
    empty_list = []
    empty_tuple = ()
    invalid_input = "not a sequence"
    
    test_cases = {
        'sample_list': sample_list,
        'sample_tuple': sample_tuple,
        'empty_list': empty_list,
        'empty_tuple': empty_tuple,
        'invalid_input': invalid_input
    }
    
    for name, case in test_cases.items():
        print(f"{name}: {get_first_element(case)}")