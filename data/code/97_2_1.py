class TruthTableGenerator:
    def generate(self, a, b, c):
        results = []
        for val_a in [0, 1]:
            for val_b in [0, 1]:
                for val_c in [0, 1]:
                    result = (val_a, val_b, val_c)
                    truth_value = "T" if (val_a or val_b or val_c) else "F"
                    results.append((val_a, val_b, val_c, truth_value))
        return results
    def display(self, results):
        print("A | B | C | A OR B OR C")
        print("---|---|---|---------")
        for a, b, c, result in results:
            print(f"{a} | {b} | {c} | {result}")
if __name__ == '__main__':
    generator = TruthTableGenerator()
    a_val = 0
    b_val = 1
    c_val = 0
    sample_results = generator.generate(a_val, b_val, c_val)
    generator.display(sample_results)