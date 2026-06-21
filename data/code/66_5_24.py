def is_sorted_ascending(lst):
    ASCENDING = 1
    DESCENDING = -1
    UNORDERED = 0

    def compare(a, b):
        if a < b:
            return ASCENDING
        elif a > b:
            return DESCENDING
        else:
            return UNORDERED

    current_order = UNORDERED
    for i in range(len(lst) - 1):
        order = compare(lst[i], lst[i + 1])
        if order == DESCENDING:
            return False
        if order == ASCENDING:
            current_order = ASCENDING

    return current_order != DESCENDING

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(is_sorted_ascending(sample_list))