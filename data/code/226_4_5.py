import operator

def repeat_list_in_place(lst):
    lst.extend(operator.mul(lst, 2))

if __name__ == '__main__':
    sample_list = ['a', 'b', 'c']
    repeat_list_in_place(sample_list)
    print(sample_list)