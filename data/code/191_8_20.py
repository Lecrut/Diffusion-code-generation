list1 = [10, 20, 30]
list2 = [40, 50, 60]

def concatenate_lists(l1, l2):
    return l1 + l2

if __name__ == '__main__':
    combined_list = concatenate_lists(list1, list2)
    print(f"List 1: {list1}")
    print(f"List 2: {list2}")
    print(f"Combined List (using direct concatenation): {combined_list}")