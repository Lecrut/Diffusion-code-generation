def pop_last(lst):
    if not lst:
        return None
    return lst.pop()

if __name__ == '__main__':
    list1 = [1, 2, 3]
    result1 = pop_last(list1)
    print(result1)
    
    list2 = []
    result2 = pop_last(list2)
    print(result2)