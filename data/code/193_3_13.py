def sum_list(lst):
    return sum(lst) if lst else 0

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40], []
    for values in sample_values:
        print(sum_list(values))