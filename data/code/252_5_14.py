def compare_sums(list1, list2):
    return sum(list1) == sum(list2)

if __name__ == '__main__':
    result1 = compare_sums([1, 2, 3, 4], [5, 6, 7, 8])
    result2 = compare_sums([10, 20, 30], [15, 5, 15])
    print(result1)
    print(result2)