def check_membership_builtin(lst, item):
    return item in lst
def check_membership_manual(lst, item):
    for element in lst:
        if element == item:
            return True
    return False
def check_membership_set_lookup(lst, item):
    s = set(lst)
    return item in s
if __name__ == '__main__':
    list1 = [1, 5, 2, 8, 3, 9]
    item1 = 8
    list2 = [100, 200, 300, 400]
    item2 = 500
    print(f"List: {list1}, Item: {item1}")
    print(f"Built-in 'in' operator result: {check_membership_builtin(list1, item1)}")
    print(f"Manual loop result: {check_membership_manual(list1, item1)}")
    print("-" * 20)
    print(f"List: {list2}, Item: {item2}")
    print(f"Built-in 'in' operator result: {check_membership_builtin(list2, item2)}")
    print(f"Manual loop result: {check_membership_manual(list2, item2)}")
    print("\nComparison using Set Lookup (for context on efficiency):")
    print(f"Set lookup result for list1 and item1: {check_membership_set_lookup(list1, item1)}")
    print(f"Set lookup result for list2 and item2: {check_membership_set_lookup(list2, item2)}")