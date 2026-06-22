def are_elements_unique(lst):
    seen = set()
    for item in lst:
        if item in seen:
            return False
        seen.add(item)
    return True
if __name__ == '__main__':
    print(are_elements_unique([1, 2, 3, 4, 5]))
    print(are_elements_unique([1, 2, 3, 3, 5]))