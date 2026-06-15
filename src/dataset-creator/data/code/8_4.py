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
    set_b = [3, 7, 2]
    result = compare_set_sums(set_a, set_b)
    if result is not None:
        print(f"Set A sum: {sum(set_a)}")
        print(f"Set B sum: {sum(set_b)}")
        print("The set with the larger sum is:")
        print(result)