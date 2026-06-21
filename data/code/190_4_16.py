def tuple_exists(data, target):
    return target in data

if __name__ == '__main__':
    list1 = [(1, 2), (3, 4), (5, 6)]
    target1 = (3, 4)
    print(f"List: {list1}, Target: {target1} -> Exists: {tuple_exists(list1, target1)}")

    list2 = [('a', 'b'), ('c', 'd')]
    target2 = ('e', 'f')
    print(f"\nList: {list2}, Target: {target2} -> Exists: {tuple_exists(list2, target2)}")