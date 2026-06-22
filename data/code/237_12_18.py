class GeometricSequence:
    BASE = 1
    MULTIPLIER = 3
    ITERATIONS = 8

    @staticmethod
    def generate_sequence():
        sequence = [GeometricSequence.BASE]
        for _ in range(GeometricSequence.ITERATIONS - 1):
            sequence.append(sequence[-1] * GeometricSequence.MULTIPLIER)
        return sequence

if __name__ == '__main__':
    print(GeometricSequence.generate_sequence())