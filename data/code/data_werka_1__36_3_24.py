import time

def reverse_string_iteratively(s):
    reversed_s = ''
    for char in s:
        reversed_s = char + reversed_s
    return reversed_s

def reverse_string_slicing(s):
    return s[::-1]

def benchmark_reverse_functions():
    long_string = 'a' * 1000000
    start_time = time.time()
    reverse_string_iteratively(long_string)
    iterative_time = time.time() - start_time
    start_time = time.time()
    reverse_string_slicing(long_string)
    slicing_time = time.time() - start_time
    if iterative_time < slicing_time:
        return ('Iterative method is faster', iterative_time)
    else:
        return ('Slicing method is faster', slicing_time)
if __name__ == '__main__':
    result, time_taken = benchmark_reverse_functions()
    print(result)
    print(f'Time taken: {time_taken} seconds')