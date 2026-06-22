def reverse_string_iteratively(s):
    reversed_s = ''
    for char in s:
        reversed_s = char + reversed_s
    return reversed_s

def reverse_string_slicing(s):
    return s[::-1]

def benchmark_reversal():
    import time
    long_string = 'a' * 1000000
    start_time = time.time()
    iteratively_reversed = reverse_string_iteratively(long_string)
    iterative_time = time.time() - start_time
    start_time = time.time()
    slicing_reversed = reverse_string_slicing(long_string)
    slicing_time = time.time() - start_time
    if iterative_time < slicing_time:
        return ('Iterative method is faster', iteratively_reversed)
    else:
        return ('Slicing method is faster', slicing_reversed)
if __name__ == '__main__':
    result, reversed_string = benchmark_reversal()
    print(result)
    print(reversed_string[:10])