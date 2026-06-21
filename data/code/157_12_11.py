def find_smallest_element(lst):
    return sorted(lst)[0]

if __name__ == '__main__':
    sample_list = [34, 7, 23, 32, 5, 62]
    print(find_smallest_element(sample_list))