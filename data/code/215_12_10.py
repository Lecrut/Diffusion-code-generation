def find_max(iterable):
    if not iterable:
        return None
    max_value = iterable[0]
    for value in iterable:
        if value > max_value:
            max_value = value
    return max_value

if __name__ == '__main__':
    sample_list = [15, 25, 5, 30, 20]
    sample_tuple = (-5, -10, -3, -8)
    empty_list = []
    
    print(f"Maximum of {sample_list}: {find_max(sample_list)}")
    print(f"Maximum of {sample_tuple}: {find_max(sample_tuple)}")
    print(f"Maximum of {empty_list}: {find_max(empty_list)}")