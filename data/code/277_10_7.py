def count_items(lst):
    if not lst:
        return 0
    count = 1
    for item in lst[1:]:
        count += 1
    return count

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(count_items(sample_list))