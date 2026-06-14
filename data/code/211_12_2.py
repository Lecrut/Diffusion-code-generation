import time
def set_difference_sorted(sample1, sample2):
    set1 = set(sample1)
    set2 = set(sample2)
    difference = set1 - set2
    return sorted(list(difference))
if __name__ == '__main__':
    sample1 = [5, 1, 8, 3, 5, 9]
    sample2 = [3, 5, 7, 1, 4]
    result = set_difference_sorted(sample1, sample2)
    print(result)