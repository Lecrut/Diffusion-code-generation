def is_sorted(lst):
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(is_sorted(sample_list))