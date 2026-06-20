def flip_bool_value(value: bool) -> bool:
    return not value

if __name__ == '__main__':
    sample_true = True
    result_true = flip_bool_value(sample_true)
    print(f"Flipping {sample_true}: {result_true}")
    
    sample_false = False
    result_false = flip_bool_value(sample_false)
    print(f"Flipping {sample_false}: {result_false}")