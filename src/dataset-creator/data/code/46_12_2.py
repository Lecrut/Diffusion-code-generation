import sys
def find_unique_elements(*lists):
    if not lists:
        return []
    all_items = set()
    for lst in lists:
        if isinstance(lst, (list, tuple)):
            all_items.update(lst)
        else:
            raise TypeError("All arguments must be iterable sequences.")
    unique_elements = {}
    for item in sorted(all_items):
        count = 0
        present_in_lists = []
        for lst in lists:
            if isinstance(lst, (list, tuple)):
                try:
                    idx = lst.index(item)
                    count += 1
                    present_in_lists.append(f"{type(lst).__name__}:{idx}")
                except ValueError:
                    pass
        if count == 1:
            unique_elements[item] = f"Present in {present_in_lists[0]}"
    return list(unique_elements.keys())
def main():
    sample_list_1 = [3, 5, 7, 9, 11]
    sample_list_2 = [4, 6, 8, 10, 12]
    sample_list_3 = [5, 11, 13, 15]
    result = find_unique_elements(sample_list_1, sample_list_2, sample_list_3)
    print("Elements present in exactly one list:")
    for item in sorted(result):
        print(item)
if __name__ == '__main__':
    main()