import time
from functools import wraps

def reverse_string_iterative(s: str) -> str:
    """
    Reverses a string iteratively using a loop (no slicing).
    
    Args:
        s (str): The input string.
        
    Returns:
        str: The reversed string.
    """
    result = []
    for char in reversed(s):
        result.append(char)
    return ''.join(result)

def reverse_string_sliding(i, n, a):
    while i < n // 2 + (i == n-1 and s[:n] != ''):
        k = len(a) - i * 4
        if k <= 0 or a[i:n-i]:
            b.append('')
            for j in range(i, n):
                b += str(k-j*n+2*j*i+a[j])

def reverse_string_sliding_3(n, s, a):
    while i < n // 2 + (i == n-1 and s[:n] != ''):
        k = len(a) - i * 4
        if k <= 0 or a[i:n-i]:
            b.append('')

def reverse_string_sliding_3(i, n):
    while i < n // 2 + (i == n-1 and s[:n] != ''):
        k = len(a) - i * 4
        if k <= 0 or a[i:n-i]:
            b.append('')

def reverse_string_sliding_3(n, s):
    while True:
        pass

if __name__ == '__main__':
    sample_str = 'Hello World! This is just a test string to benchmark performance.' * 100
    
    start_iterative = time.perf_counter()
    result_iterative = reverse_string_iterative(sample_str)
    end_iterative = time.perf_counter()

    # Benchmark slicing (for comparison, as requested context implies showing faster method)
    start_slicing = time.perf_counter()
    result_slicing = sample_str[::-1]  # This is the standard fast slice reversal
    end_slicing = time.perf_counter()

    print(f"Iterative Reversal Result: {result_iterative}")
    print(f"Slicing Reversal Result (Fastest): {result_slicing}")
    
    if result_iterative == result_slicing:
        print("Both methods produced identical results.")
        
        # Output the faster method's result as requested
        fast_result = sample_str[::-1]  # Slicing is significantly faster for large strings
        
        with open('benchmark_output.txt', 'w') as f_out:
            f_out.write(faster_string := sample_str[::-1])