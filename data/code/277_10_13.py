def count_items(lst):
    COUNT_INITIAL = 0
    count = COUNT_INITIAL
    for item in lst:
        count += 1
    return count

if __name__ == '__main__':
    SAMPLE_LIST = [1, 2, 3, 4, 5]
    print(count_items(SAMPLE_LIST))