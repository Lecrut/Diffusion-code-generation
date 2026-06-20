def check_at_least_one(iterable):
    return any(iterable)

if __name__ == '__main__':
    list1 = [False, False, False]
    list2 = [True, False, False]
    list3 = []
    print(f"list1: {check_at_least_one(list1)}")
    print(f"list2: {check_at_least_one(list2)}")
    print(f"list3: {check_at_least_one(list3)}")