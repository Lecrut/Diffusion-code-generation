def contains_duplicates(lst):
    seen = set()
    for item in lst:
        if item in seen:
            return True
        seen.add(item)
    return False

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5]
    sample_list2 = [1, 2, 3, 3, 4, 5]

    print(f"List {sample_list1} contains duplicates: {contains_duplicates(sample_list1)}")
    print(f"List {sample_list2} contains duplicates: {contains_duplicates(sample_list2)}")