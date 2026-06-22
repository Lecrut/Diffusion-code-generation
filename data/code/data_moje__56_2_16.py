def multiplication_table_generator(n):
    limit = 10
    current_multiplier = 1
    while current_multiplier <= limit:
        product = n * current_multiplier
        yield current_multiplier, product
        current_multiplier += 1

if __name__ == '__main__':
    target_number = 12
    generator_instance = multiplication_table_generator(target_number)
    for multiplier, result in generator_instance:
        print(f"{target_number} * {multiplier} = {result}")