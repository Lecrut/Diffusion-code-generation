def are_elements_unique(lst):
    return len(lst) == len(set(lst))

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(are_elements_unique(sample_list))