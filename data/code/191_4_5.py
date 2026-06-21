TUPLE_LIST1 = [(1, 'a'), (2, 'b')]
TUPLE_LIST2 = [(3, 'c'), (4, 'd')]

def extend_tuples(list1, list2):
    return list1 + list2

if __name__ == '__main__':
    result = extend_tuples(TUPLE_LIST1, TUPLE_LIST2)
    print(result)