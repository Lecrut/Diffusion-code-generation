import timeit
def has_positive_value(numbers):
    return any(n > 0 for n in numbers)
if __name__ == '__main__':
    test_data = [1, -2, 3.5]
    iterations = 1_000_000
    start_time = timeit.default_timer()
    result = has_positive_value(test_data)
    end_time = timeit.default_timer()
    print(f"Result: {result}")
    print(f"Time taken for {iterations} calls: {(end_time - start_time):.4f}s")