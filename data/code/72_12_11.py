def find_inequalities(lst):
    inequalities = []
    for i in range(len(lst) - 1):
        if lst[i] != lst[i + 1]:
            inequalities.append((i, lst[i], lst[i + 1]))
    return inequalities

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    print(find_inequalities(sample_list))