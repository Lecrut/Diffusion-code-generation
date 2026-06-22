class GeometricSequenceGenerator:
    START = 5
    RATIO = 3

    @staticmethod
    def generate_sequence(terms):
        return [GeometricSequenceGenerator.START * (GeometricSequenceGenerator.RATIO ** i) for i in range(terms)]

if __name__ == '__main__':
    result = GeometricSequenceGenerator.generate_sequence(8)
    print(result)