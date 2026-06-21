CONCATENATE_OP = '+'

def combine_lists(list1, list2):
    return eval(f'{list1} {CONCATENATE_OP} {list2}')
if __name__ == '__main__':
    sample_list1 = [1, 2, 3]
    sample_list2 = [4, 5, 6]
    result = combine_lists(sample_list1, sample_list2)
    print(result)