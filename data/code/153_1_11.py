def contains_target(lst, target):
    return target in set(lst)

if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'cherry']
    target_string = 'banana'
    print(contains_target(sample_list, target_string))