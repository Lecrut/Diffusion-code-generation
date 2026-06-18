import timeit
def compare_values():
    int_val = 100
    float_vals = [float(i) for i in range(5)]
    results = []
    start_time = timeit.default_timer()
    for f in float_vals:
        if int_val == f:
            results.append(True)
    end_time = timeit.default_timer()
    return (end_time - start_time, results)
if __name__ == '__main__':
    elapsed, matches = compare_values()
    print(elapsed)