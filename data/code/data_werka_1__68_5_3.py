def consecutive_diffs(lst):
    for i in range(1, len(lst)):
        yield abs(lst[i] - lst[i - 1])

if __name__ == '__main__':
    sample_list = [5, 3, 8, 1, 4]
    diffs = list(consecutive_diffs(sample_list))
    print(diffs)