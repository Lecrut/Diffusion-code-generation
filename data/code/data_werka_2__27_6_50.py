def are_sums_different(list1, list2):
    def calculate_sum(numbers):
        total = 0
        for number in numbers:
            total += number
        return total

    sum1 = calculate_sum(list1)
    sum2 = calculate_sum(list2)
    return sum1 != sum2

if __name__ == '__main__':
    SAMPLE_LIST_1 = [7, 8, 9, 10, 11]
    SAMPLE_LIST_2 = [11, 10, 9, 8, 7]
    result = are_sums_different(SAMPLE_LIST_1, SAMPLE_LIST_2)
    print(result)