def contains_target(iterable: any, target) -> bool:
    try:
        return target in iterable
    except TypeError as e:
        raise ValueError(f"Input must be an iterable, got {type(iterable).__name__}. Error details: {e}") from e
if __name__ == '__main__':
    sample_list = [10, 20, 30]
    sample_tuple = (40, 50)
    sample_set = {60}
    target_to_find = 20
    result_list = contains_target(sample_list, target_to_find)
    print(f"Found in list: {result_list}")
    target_not_found = 99
    result_tuple = contains_target(sample_tuple, target_not_found)
    print(f"Not found in tuple: {result_tuple}")