def check_endpoints(iterable):
    try:
        first = next(iter(iterable))
    except StopIteration:
        return None, None
    try:
        last = next(reversed(iterable))
    except StopIteration:
        return first, first
    return first, last
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [10]
    list3 = []
    list4 = ['a', 'b']
    list5 = []
    list6 = [99]
    print(f"List 1: {check_endpoints(list1)}")
    print(f"List 2: {check_endpoints(list2)}")
    print(f"List 3: {check_endpoints(list3)}")
    print(f"List 4: {check_endpoints(list4)}")
    print(f"List 5: {check_endpoints(list5)}")
    print(f"List 6: {check_endpoints(list6)}")