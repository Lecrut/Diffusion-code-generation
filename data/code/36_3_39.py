def reverse_string_iteratively(s):
    reversed_str = ''
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

def reverse_string_slicing(s):
    return s[::-1]

def benchmark_reverse_methods():
    import time
    long_string = 'a' * 10 ** 6
    start_time = time.time()
    reverse_string_iteratively(long_string)
    iterative_time = time.time() - start_time
    start_time = time.time()
    reverse_string_slicing(long_string)
    slicing_time = time.time() - start_time
    if iterative_time < slicing_time:
        return 'Iterative method is faster'
    else:
        return 'Slicing method is faster'
if __name__ == '__main__':
    result = benchmark_reverse_methods()
    print(result)