def product_generator(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(i + 1, n):
            yield numbers[i] * numbers[j]
if __name__ == '__main__':
    input_list = [1, 2, 3]
    result_generator = product_generator(input_list)
    for product in result_generator:
        print(product)