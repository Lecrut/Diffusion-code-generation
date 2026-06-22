class NumberSequenceGenerator:
    SEPARATOR = ','

    @staticmethod
    def generate_sequence(n):
        return NumberSequenceGenerator.SEPARATOR.join(str(i) for i in range(1, n + 1))

if __name__ == '__main__':
    N = 5
    result = NumberSequenceGenerator.generate_sequence(N)
    print(result)