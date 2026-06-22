class ArithmeticProgression:
    START = 3
    DIFFERENCE = 4

    @staticmethod
    def generate_terms(n):
        return [ArithmeticProgression.START + i * ArithmeticProgression.DIFFERENCE for i in range(n)]

if __name__ == '__main__':
    terms = ArithmeticProgression.generate_terms(15)
    print(terms)