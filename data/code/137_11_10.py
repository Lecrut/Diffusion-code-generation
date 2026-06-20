def has_duplicates(lst):
    seen = set()
    for item in lst:
        if item in seen:
            return True
        seen.add(item)
    return False

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5]
    sample_list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
    print(f"List {sample_list1} has duplicates: {has_duplicates(sample_list1)}")
    print(f"List {sample_list2} has duplicates: {has_duplicates(sample_list2)}")