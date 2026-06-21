TOTAL_LISTS = 3
if __name__ == '__main__':
    sample_lists = [[1, 2, 3, 4, 5], [10, 20, 30, 40], [-1, 5, -3, 10]]
    total_sums = [sum((x for x in lst)) for lst in sample_lists]
    print(total_sums)