def find_max(iterable):
    if not iterable:
        return None
    maximum = iterable[0]
    for number in iterable:
        if number > maximum:
            maximum = number
    return maximum

if __name__ == '__main__':
    sample_list = [15, 25, 10, 30, 5]
    another_sample_list = [-5, -10, -3, -8]
    empty_list = []
    
    print(f"Maximum of {sample_list}: {find_max(sample_list)}")
    print(f"Maximum of {another_sample_list}: {find_max(another_sample_list)}")
    print(f"Maximum of {empty_list}: {find_max(empty_list)}")