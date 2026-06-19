def find_middle_element(lst):
    if not lst:
        raise ValueError("List cannot be empty")
    n = len(lst)
    return lst[n // 2]

if __name__ == '__main__':
    sample_list = [5.5, 6.6, 7.7, 8.8, 9.9]
    print(find_middle_element(sample_list))