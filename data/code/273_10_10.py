def perform_sequence():
    greeting = 'Hello'
    sum_result = 2 + 3
    product_result = sum_result * 4
    return greeting, product_result

if __name__ == '__main__':
    for _ in range(3):
        greeting, result = perform_sequence()
        print(greeting)
        print(result)