class Fibonacci:
    def __init__(self):
        self.base_matrix = [[1, 1], [1, 0]]

    def _multiply(self, A, B):
        C = [[0, 0], [0, 0]]
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    C[i][j] += A[i][k] * B[k][j]
        return C

    def _power(self, M, n):
        result = [[1, 0], [0, 1]]
        base = M
        while n > 0:
            if n % 2 == 1:
                result = self._multiply(result, base)
            base = self._multiply(base, base)
            n //= 2
        return result

    def get_term(self, n):
        if n <= 0:
            return 0
        if n == 1:
            return 1
        result_matrix = self._power(self.base_matrix, n - 1)
        return result_matrix[0][0]

if __name__ == '__main__':
    fib = Fibonacci()
    for i in range(1, 11):
        print(f"Fibonacci({i}) = {fib.get_term(i)}")
    print(f"Fibonacci(50) = {fib.get_term(50)}")