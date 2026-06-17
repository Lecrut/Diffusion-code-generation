def product_of_list(numbers):
    product = 1
    for number in numbers:
        product *= number
    return product
if __name__ == '__main__':
    list1 = [1, 2, 3, 4]
    result1 = product_of_list(list1)
    print(result1)
    list2 = [5, -2, 10]
    result2 = product_of_list(list2)
    print(result2)
    list3 = [7]
    result3 = product_of_list(list3)
    print(result3)
    list4 = [0, 5, 10]
    result4 = product_of_list(list4)
    print(result4)