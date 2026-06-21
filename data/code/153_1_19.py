def contains_target(target, lst):
    return target in set(lst)

if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'cherry']
    target_string = 'banana'
    print(contains_target(target_string, sample_list))