def reverse_string_iteratively(s):
    reversed_str = ''
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

def reverse_string_slicing(s):
    return s[::-1]

def benchmark_reverse_methods():
    long_string = 'a' * 10 ** 6
    import time
    start_time = time.time()
    iteratively_reversed = reverse_string_iteratively(long_string)
    iteratively_time = time.time() - start_time
    start_time = time.time()
    slicing_reversed = reverse_string_slicing(long_string)
    slicing_time = time.time() - start_time
    if iteratively_time < slicing_time:
        return ('Iterative method is faster', iteratively_reversed)
    else:
        return ('Slicing method is faster', slicing_reversed)
if __name__ == '__main__':
    result, reversed_string = benchmark_reverse_methods()
    print(result)
    print(reversed_string[:10])