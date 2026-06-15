def consecutive_product_generator(limit):
    current_product = 1
    for i in range(1, limit + 1):
        current_product *= i
        yield current_product
if __name__ == '__main__':
    test_limit = 5
    generator = consecutive_product_generator(test_limit)
    results = list(generator)
    print(f"Limit: {test_limit}")
    print("Results:")
    for result in results:
        print(result)