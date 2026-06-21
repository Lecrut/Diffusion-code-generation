def check_zero_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result == 0:
            print("Zero detected.")
        else:
            print(f"Non-zero result: {result}")
        return result
    return wrapper

@check_zero_result
def calculate_sum(a, b):
    return a + b

@check_zero_result
def calculate_product(a, b):
    return a * b

if __name__ == '__main__':
    sum_result = calculate_sum(10, -10)
    print(sum_result)
    product_result = calculate_product(4, 5)
    print(product_result)