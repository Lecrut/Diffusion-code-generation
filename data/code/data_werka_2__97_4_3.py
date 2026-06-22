class TruthTableGenerator:
    def generate(self):
        results = []
        for a in [0, 1]:
            for b in [0, 1]:
                results.append((a, b))
        return results

if __name__ == '__main__':
    generator = TruthTableGenerator()
    print(generator.generate())