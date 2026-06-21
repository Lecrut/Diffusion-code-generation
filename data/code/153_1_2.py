def find_target(target, lst):
    return target in set(lst)

if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'cherry']
    target_string = 'banana'
    print(find_target(target_string, sample_list))