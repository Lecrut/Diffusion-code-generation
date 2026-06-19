def reverse_string_iteratively(s):
    reversed_s = ''
    for char in s:
        reversed_s = char + reversed_s
    return reversed_s

def reverse_string_slicing(s):
    return s[::-1]

def benchmark_reverse_methods():
    long_string = 'a' * 10 ** 6
    import time
    start_time = time.time()
    reverse_string_iteratively(long_string)
    iter_time = time.time() - start_time
    start_time = time.time()
    reverse_string_slicing(long_string)
    slice_time = time.time() - start_time
    if iter_time < slice_time:
        return ('Iterative method is faster', iter_time)
    else:
        return ('Slicing method is faster', slice_time)
if __name__ == '__main__':
    result, time_taken = benchmark_reverse_methods()
    print(result)
    print(f'Time taken: {time_taken:.6f} seconds')