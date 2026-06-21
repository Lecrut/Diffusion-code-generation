def is_float_in_list(target, float_list):
    if not isinstance(float_list, list) or not all(isinstance(x, float) for x in float_list):
        raise ValueError("The second argument must be a list of floats.")
    if not isinstance(target, float):
        raise ValueError("The first argument must be a float.")
    
    return any(abs(target - num) < 1e-9 for num in float_list)

if __name__ == '__main__':
    sample_list = [0.1 + 0.2, 0.3, 0.4]
    target_value = 0.5
    print(is_float_in_list(target_value, sample_list))