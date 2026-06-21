def is_lexicographically_smaller(list1, list2):
    for a, b in zip(list1, list2):
        if a < b:
            return True
        elif a > b:
            return False
    return len(list1) < len(list2)
if __name__ == '__main__':
    print(is_lexicographically_smaller([1, 2, 3], [1, 2, 4]))
    print(is_lexicographically_smaller([1, 2, 4], [1, 2, 3]))
    print(is_lexicographically_smaller([1, 2], [1, 2, 3]))
    print(is_lexicographically_smaller([1, 2, 3], [1, 2]))