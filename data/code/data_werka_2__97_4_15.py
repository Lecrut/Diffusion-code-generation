class TruthTableGenerator:
    def generate(self):
        results = []
        for a in [False, True]:
            for b in [False, True]:
                results.append((a, b))
        return results

if __name__ == '__main__':
    generator = TruthTableGenerator()
    print(generator.generate())