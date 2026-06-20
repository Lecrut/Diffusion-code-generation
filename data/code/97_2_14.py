class TruthTableGenerator:
    def __init__(self):
        self.header = "A | B | C | A AND B | A OR C | B XOR C"
    
    def generate(self, inputs):
        results = []
        for vals in inputs:
            a, b, c = vals
            ab = a & b
            ac = a | c
            bc = b ^ c
            result = (a, b, c, ab, ac, bc)
            results.append(result)
        return results
    
    def display(self, results):
        print(self.header)
        print("-" * len(self.header))
        for a, b, c, ab, ac, bc in results:
            print(f"{a} | {b} | {c} | {ab} | {ac} | {bc}")

if __name__ == '__main__':
    generator = TruthTableGenerator()
    inputs = [(0, 0, 0), (0, 1, 0), (1, 0, 0), (1, 1, 0),
              (0, 0, 1), (0, 1, 1), (1, 0, 1), (1, 1, 1)]
    results = generator.generate(inputs)
    generator.display(results)