def compare_set_sums(set1, set2):
    sum1 = sum(set1)
    sum2 = sum(set2)
    if sum1 > sum2:
        return set1
    elif sum2 > sum1:
        return set2
    else:
        return None
if __name__ == '__main__':
    set_a = [1, 5, 10]
    set_b = [3, 7, 4]
    result = compare_set_sums(set_a, set_b)
    if result:
        print(f"Set with larger sum: {result}")