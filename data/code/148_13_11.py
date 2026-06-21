def find_max_element(lst):
    if not lst:
        raise ValueError("Input list is empty")
    return max(lst)

if __name__ == '__main__':
    sample_list = [3.5, 1.2, 4.8, 2.9]
    print(find_max_element(sample_list))