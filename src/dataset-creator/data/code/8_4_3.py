import sys
def compare_set_sums(set1, set2):
    sum1 = sum(set1)
    sum2 = sum(set2)
    if sum1 > sum2:
        return set1, sum1
    elif sum2 > sum1:
        return set2, sum2
    else:
        return None, sum1
if __name__ == '__main__':
    set_a = [10, 20, 30]
    set_b = [5, 15, 25]
    result_set, result_sum = compare_set_sums(set_a, set_b)
    if result_set:
        print(f"Set with the larger sum: {result_set}")
        print(f"Sum: {result_sum}")