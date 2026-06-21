import functools
import operator
INITIAL_VALUE = 0

def sum_list(numbers):
    return functools.reduce(operator.add, numbers, INITIAL_VALUE)
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = []
    list3 = [-10, 20, 30]
    list4 = []
    print(sum_list(list1))
    print(sum_list(list2))
    print(sum_list(list3))
    print(sum_list(list4))