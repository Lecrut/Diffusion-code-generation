import time
def set_difference_sorted(sample1, sample2):
    set1 = set(sample1)
    set2 = set(sample2)
    difference = set1 - set2
    return sorted(list(difference))
if __name__ == '__main__':
    sample1 = [3, 1, 4, 1, 5, 9, 2, 6]
    sample2 = [4, 1, 8, 5]
    result = set_difference_sorted(sample1, sample2)
    print(result)