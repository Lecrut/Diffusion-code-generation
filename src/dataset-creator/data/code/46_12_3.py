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
        present_in = []
        for lst in lists:
            if isinstance(lst, (list, tuple)) and item in lst:
                count += 1
                present_in.append(str(type(item).__name__))
        if count == 1:
            unique_elements[item] = True
    return list(unique_elements.keys())
def main():
    sample_lists = [
        ["apple", "banana", "cherry"],
        ["banana", "date", "elderberry"]
    ]
    result = find_unique_elements(*sample_lists)
    print("Elements present in exactly one list:")
    for item in sorted(result):
        print(item)
if __name__ == '__main__':
    main()