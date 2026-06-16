def product_of_list(numbers):
    product = 1
    for number in numbers:
        product *= number
    return product
if __name__ == '__main__':
    list1 = [1, 2, 3, 4]
    print(product_of_list(list1))
    list2 = [5, -2, 10]
    print(product_of_list(list2))
    list3 = [7]
    print(product_of_list(list3))
    list4 = [0, 5, 2]
    print(product_of_list(list4))