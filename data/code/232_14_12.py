class NumberSequence:
    MAX_ITERATIONS = 5

    @staticmethod
    def square_sequence(n):
        return [i**2 for i in range(1, n+1)]

if __name__ == '__main__':
    result = NumberSequence.square_sequence(NumberSequence.MAX_ITERATIONS)
    print(result)