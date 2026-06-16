import timeit
def compare_types():
    a = 100
    b = float('inf')
    result_a = (a == b)
    result_b = (b == a)
    return {
        'int_equals_float': result_a,
        'float_equals_int': result_b,
        'type_of_result_a': type(result_a),
        'type_of_result_b': type(result_b)
    }
if __name__ == '__main__':
    iterations = 10_000_000
    setup_code = "a=1; b=float('inf'); result=(a==b)"
    elapsed_time = timeit.timeit(setup_code, number=iterations)
    print(f"Performance Test: {elapsed_time:.4f} seconds for {iterations:,} comparisons")
    comparison_results = compare_types()
    print("Type Coercion Results:", comparison_results)