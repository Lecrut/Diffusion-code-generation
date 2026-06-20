def has_duplicates(lst):
    seen = set()
    for item in lst:
        if item in seen:
            return True
        seen.add(item)
    return False
if __name__ == '__main__':
    print(has_duplicates([1, 2, 3, 4, 5]))
    print(has_duplicates([1, 2, 3, 3, 5]))