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
    for item in all_items:
        count = 0
        present_in_lists = []
        for lst in lists:
            if isinstance(item, (int, float)) and not isinstance(lst[0], str):
                try:
                    idx = lst.index(item)
                    count += 1
                    present_in_lists.append(True)
                except ValueError:
                    pass
            elif isinstance(item, str):
                if item in [str(x).strip() for x in lst]:
                    count += 1
        if count == 1:
            unique_elements[item] = True
    return list(unique_elements.keys())
def main():
    sample_lists = [[1, 2, 3], [4, 5, 6]]
    try:
        result = find_unique_elements(*sample_lists)
        print(f"Elements present in exactly one list: {result}")
        if not isinstance(result[0], int):
            unique_strs = []
            for item in result:
                unique_strs.append(item.strip())
            print(f"Unique strings (exactly once): {unique_strs}")
    except TypeError as e:
        print(f"Error: Invalid input type. {e}", file=sys.stderr)
if __name__ == '__main__':
    main()