MAX_SIZE = 100

def contains_duplicates(lst):
    seen = [False] * MAX_SIZE
    for item in lst:
        if seen[item]:
            return True
        seen[item] = True
    return False
if __name__ == '__main__':
    print(contains_duplicates([1, 2, 3, 4, 5]))
    print(contains_duplicates([1, 2, 3, 3, 5]))