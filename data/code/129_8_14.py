def stable_sort_mixed(lst):
    return sorted(lst, key=str)

if __name__ == '__main__':
    mixed_list = ['apple', 3, 'banana', 1, 'cherry', 2]
    print(stable_sort_mixed(mixed_list))