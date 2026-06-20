def stable_sort_mixed(lst):
    return sorted(lst, key=lambda x: str(x))

if __name__ == '__main__':
    sample_list = [3, 'apple', 2, 'banana', '1', 4]
    print(stable_sort_mixed(sample_list))