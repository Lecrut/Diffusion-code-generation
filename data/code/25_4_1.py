def check_for_zero(data):
    for item in data:
        if item == 0:
            yield True
            return
    yield False
if __name__ == '__main__':
    list1 = [1, 2, 3, 4]
    list2 = [1, 0, 3, 4]
    list3 = [5, 6, 7, 8]
    list4 = [0, 1, 2, 3]
    empty_list = []
    print(f"List 1: {list1}")
    print(f"Result: {list(check_for_zero(list1))}")
    print("-" * 20)
    print(f"List 2: {list2}")
    print(f"Result: {list(check_for_zero(list2))}")
    print("-" * 20)
    print(f"List 3: {list3}")
    print(f"Result: {list(check_for_zero(list3))}")
    print("-" * 20)
    print(f"List 4: {list4}")
    print(f"Result: {list(check_for_zero(list4))}")
    print("-" * 20)
    print(f"Empty List: {empty_list}")
    print(f"Result: {list(check_for_zero(empty_list))}")