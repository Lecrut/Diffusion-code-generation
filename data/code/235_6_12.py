class PyramidGenerator:
    @staticmethod
    def generate_pyramid(n):
        for i in range(1, n + 1):
            yield " " * (n - i) + "+" * (2 * i - 1)

if __name__ == '__main__':
    N = 5
    pyramid = PyramidGenerator.generate_pyramid(N)
    for line in pyramid:
        print(line)