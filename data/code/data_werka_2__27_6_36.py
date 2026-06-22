def are_sums_different(list1, list2):
    SUM_THRESHOLD = 0

    def calculate_sum(numbers):
        total = 0
        for number in numbers:
            total += number
        return total
    sum1 = calculate_sum(list1)
    sum2 = calculate_sum(list2)
    return abs(sum1 - sum2) > SUM_THRESHOLD
if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5]
    sample_list2 = [5, 4, 3, 2, 1]
    result = are_sums_different(sample_list1, sample_list2)
    print(result)