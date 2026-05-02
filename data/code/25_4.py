def check_for_zero(data):
    for item in data:
        if item == 0:
            yield True
            return
    yield False
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [1, 0, 3, 4, 5]
    list3 = [10, 20, 30]
    list4 = [0, 5, 10]
    list5 = []
    print(f"List 1: {list1} -> {list(check_for_zero(list1))}")
    print(f"List 2: {list2} -> {list(check_for_zero(list2))}")
    print(f"List 3: {list3} -> {list(check_for_zero(list3))}")
    print(f"List 4: {list4} -> {list(check_for_zero(list4))}")
    print(f"List 5: {list5} -> {list(check_for_zero(list5))}")