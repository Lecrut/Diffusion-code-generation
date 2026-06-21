def find_smallest(lst):
    return sorted(lst)[0]

if __name__ == '__main__':
    sample_list = [5, 3, 8, 1, 2]
    print(find_smallest(sample_list))