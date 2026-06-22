def find_min(lst):
    if not lst:
        raise ValueError("List cannot be empty")
    return min(lst)

if __name__ == '__main__':
    sample_list = [3, 5, 1, 2, 4]
    print(find_min(sample_list))