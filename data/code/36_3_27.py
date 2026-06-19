def reverse_string_iteratively(s):
    reversed_s = ''
    for char in s:
        reversed_s = char + reversed_s
    return reversed_s

def reverse_string_with_slicing(s):
    return s[::-1]

def benchmark_reverse_functions():
    import time
    long_string = 'a' * 1000000
    start_time = time.time()
    reverse_string_iteratively(long_string)
    iterative_time = time.time() - start_time
    start_time = time.time()
    reverse_string_with_slicing(long_string)
    slicing_time = time.time() - start_time
    if iterative_time < slicing_time:
        return 'Iterative method is faster'
    else:
        return 'Slicing method is faster'
if __name__ == '__main__':
    result = benchmark_reverse_functions()
    print(result)