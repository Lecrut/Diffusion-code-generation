def product_of_evens(numbers):
    if not numbers:
        return 1
    even_numbers = [num for num in numbers if num % 2 == 0]
    product = 1
    for num in even_numbers:
        product *= num
    return product
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5, 6]
    list2 = [1, 3, 5, 7]
    list3 = [2, 4, 6, 8, 10]
    list4 = []
    list5 = [10, 15, 20]
    print(product_of_evens(list1))
    print(product_of_evens(list2))
    print(product_of_evens(list3))
    print(product_of_evens(list4))
    print(product_of_evens(list5))