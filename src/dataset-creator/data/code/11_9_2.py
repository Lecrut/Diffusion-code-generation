def consecutive_product_generator(limit):
    current_product = 1
    for i in range(1, limit + 1):
        current_product *= i
        yield current_product
if __name__ == '__main__':
    limit = 5
    generator = consecutive_product_generator(limit)
    results = list(generator)
    print(f"Limit: {limit}")
    print(f"Results of multiplying consecutive integers from 1 to {limit}: {results}")