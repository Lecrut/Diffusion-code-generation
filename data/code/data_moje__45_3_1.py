def find_min(lst):
    return min(lst) if lst else None

if __name__ == '__main__':
    sample = [3, 1, 4, 1, 5, 9, 2, 6]
    result = find_min(sample)
    print(result)