def compare_sums(list1, list2):
    sum1 = sum(list1)
    sum2 = sum(list2)
    return sum1 == sum2

if __name__ == '__main__':
    sample_list1 = [10, 20, 30]
    sample_list2 = [15, 15, 20]
    result = compare_sums(sample_list1, sample_list2)
    print(result)