import operator

def repeat_list_in_place(lst):
    lst.extend(operator.mul(lst, 2))

if __name__ == '__main__':
    sample = ['a', 'b', 'c']
    repeat_list_in_place(sample)
    print(sample)