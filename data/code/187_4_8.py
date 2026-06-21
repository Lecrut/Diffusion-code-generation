def find_largest_element(lst):
    if not lst:
        return None
    return max(lst)

if __name__ == '__main__':
    sample_list = [3, 5, 1, 2, 4]
    print(find_largest_element(sample_list))