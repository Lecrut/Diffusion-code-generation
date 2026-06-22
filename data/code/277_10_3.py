def count_items(lst):
    if not isinstance(lst, list):
        raise ValueError("Input must be a list")
    count = 0
    for item in lst:
        count += 1
    return count

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(count_items(sample_list))