def find_min_mixed(lst):
    return min(float(x) for x in lst)

if __name__ == '__main__':
    sample = [3, 5.5, '2', 4]
    print(find_min_mixed(sample))