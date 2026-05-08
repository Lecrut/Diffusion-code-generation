class TruthTableGenerator:
    def generate(self, a, b, c):
        results = []
        for val_a in [0, 1]:
            for val_b in [0, 1]:
                for val_c in [0, 1]:
                    result = (val_a, val_b, val_c)
                    results.append(result)
        return results
    def display(self, results):
        print("A | B | C | A AND B | A AND C | B AND C | A AND B AND C")
        print("-" * 60)
        for a, b, c in results:
            ab = a & b
            ac = a & c
            bc = b & c
            abc = a & b & c
            print(f"{a} | {b} | {c} | {ab} | {ac} | {bc} | {abc}")
if __name__ == '__main__':
    generator = TruthTableGenerator()
    a_val = 0
    b_val = 1
    c_val = 0
    all_results = generator.generate(a_val, b_val, c_val)
    generator.display(all_results)