import numpy as np

def compute_fibonacci(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    def matrix_mult(A, B):
        return np.dot(A, B)
    
    def matrix_pow(M, p):
        result = np.eye(len(M), dtype=object)
        base = np.array(M, dtype=object)
        while p > 0:
            if p % 2 == 1:
                result = matrix_mult(result, base)
            base = matrix_mult(base, base)
            p //= 2
        return result
    
    M = np.array([[1, 1], [1, 0]], dtype=object)
    result_matrix = matrix_pow(M, n)
    return int(result_matrix[0, 1])

if __name__ == '__main__':
    for i in range(50):
        print(f"Fib({i}) = {compute_fibonacci(i)}")