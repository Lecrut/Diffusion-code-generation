def is_sorted_ascending(lst):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True

if __name__ == '__main__':
    sample_list = [5, 6, 7, 8, 9]
    print(is_sorted_ascending(sample_list))