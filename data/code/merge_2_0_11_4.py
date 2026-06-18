import timeit
def compare_values():
    int_val = 1000000000
    float_val = 999999999.5
    result_int_float = (int_val == float_val)
    return {
        'type_coercion_result': result_int_float,
        'execution_time_ns': timeit.timeit(stmt='10**6', number=1)*1e9
    }
if __name__ == '__main__':
    output = compare_values()
    print(f"Type coercion check (int vs float): {output['type_coercion_result']}")
    print(f"Performance benchmark time: {output['execution_time_ns']:.2f} ns")