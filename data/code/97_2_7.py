class TruthTableGenerator:
    def generate(self, a, b, c):
        results = []
        for val_a in [0, 1]:
            for val_b in [0, 1]:
                for val_c in [0, 1]:
                    result = (val_a, val_b, val_c)
                    print(f"A={val_a}, B={val_b}, C={val_c}:")
                    results.append((val_a, val_b, val_c))
        return results
if __name__ == '__main__':
    generator = TruthTableGenerator()
    generator.generate(0, 0, 0)