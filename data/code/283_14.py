def contains_duplicates(input_list):
    seen = set()
    for item in input_list:
        if item in seen:
            return True
        seen.add(item)
    return False
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [1, 2, 3, 4, 1]
    list3 = ['a', 'b', 'c', 'a']
    list4 = []
    list5 = [5, 5, 5, 5]
    print(f"List 1 has duplicates: {contains_duplicates(list1)}")
    print(f"List 2 has duplicates: {contains_duplicates(list2)}")
    print(f"List 3 has duplicates: {contains_duplicates(list3)}")
    print(f"List 4 has duplicates: {contains_duplicates(list4)}")
    print(f"List 5 has duplicates: {contains_duplicates(list5)}")