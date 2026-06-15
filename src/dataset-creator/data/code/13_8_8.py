def sequential_product_sum(numbers):
    if len(numbers) < 2:
        return 0
    total_sum = 0
    for i in range(len(numbers) - 1):
        product = numbers[i] * numbers[i+1]
        total_sum += product
    return total_sum
if __name__ == '__main__':
    list1 = [1, 2, 3, 4]
    result1 = sequential_product_sum(list1)
    print(result1)
    list2 = [5, 10, 2, 8]
    result2 = sequential_product_sum(list2)
    print(result2)
    list3 = [1, 1, 1, 1]
    result3 = sequential_product_sum(list3)
    print(result3)
    list4 = [10, 5]
    result4 = sequential_product_sum(list4)
    print(result4)