class ArithmeticProgression:
    START = 5
    DIFFERENCE = 3

    @staticmethod
    def generate_sequence(terms=15):
        return [ArithmeticProgression.START + i * ArithmeticProgression.DIFFERENCE for i in range(terms)]

if __name__ == '__main__':
    progression = ArithmeticProgression.generate_sequence()
    print(progression)