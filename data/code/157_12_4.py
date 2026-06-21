def find_smallest(lst):
    return sorted(lst)[0]

if __name__ == '__main__':
    sample_list = [34, 7, 23, 32, 5, 62]
    print(find_smallest(sample_list))