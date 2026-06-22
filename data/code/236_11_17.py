def repeat_tuple(base_tuple, multiplier):
    return base_tuple * multiplier

if __name__ == '__main__':
    sample_base_tuple = (1, 2, 3)
    sample_multiplier = 5
    result = repeat_tuple(sample_base_tuple, sample_multiplier)
    print(f"Base Tuple: {sample_base_tuple}, Multiplier: {sample_multiplier}")
    print("Result:")
    for item in result:
        print(item)