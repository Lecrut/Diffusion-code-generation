def is_lexicographically_smaller(list1, list2):
    for i in range(min(len(list1), len(list2))):
        if list1[i] < list2[i]:
            return True
        elif list1[i] > list2[i]:
            return False
    return len(list1) < len(list2)
if __name__ == '__main__':
    print(is_lexicographically_smaller([1, 2], [3, 4]))
    print(is_lexicographically_smaller([1, 2], [1, 2]))
    print(is_lexicographically_smaller([1, 2, 3], [1, 2]))