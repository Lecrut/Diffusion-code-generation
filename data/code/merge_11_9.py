def consecutive_product_generator(limit):
    current_product = 1
    for i in range(1, limit + 1):
        current_product *= i
        yield current_product
if __name__ == '__main__':
    limit_value = 5
    generator = consecutive_product_generator(limit_value)
    results = list(generator)
    print(f"Limit: {limit_value}")
    print("Results of multiplying consecutive integers from 1 to N:")
    for result in results:
        print(result)