class TriangularSequence:
    @staticmethod
    def generate_terms(n):
        return [sum(range(i+1)) for i in range(1, n+1)]

if __name__ == '__main__':
    terms = TriangularSequence.generate_terms(12)
    print(terms)