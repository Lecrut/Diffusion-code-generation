def sequential_product_sum(numbers):
    if len(numbers) < 2:
        return 0
    total_sum = 0
    for i in range(len(numbers) - 1):
        total_sum += numbers[i] * numbers[i+1]
    return total_sum
if __name__ == '__main__':
    list1 = [1, 2, 3, 4]
    result1 = sequential_product_sum(list1)
    print(result1)
    list2 = [5, 10, 2, 8]
    result2 = sequential_product_sum(list2)
    print(result2)
    list3 = [10, 20]
    result3 = sequential_product_sum(list3)
    print(result3)
    list4 = [7]
    result4 = sequential_product_sum(list4)
    print(result4)