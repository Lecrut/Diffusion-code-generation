class TruthTableGenerator:
    def generate(self, a, b, c):
        results = []
        for val_a in [0, 1]:
            for val_b in [0, 1]:
                for val_c in [0, 1]:
                    result = (val_a, val_b, val_c)
                    truth_value = str(val_a) + " " + str(val_b) + " " + str(val_c)
                    results.append((result, truth_value))
        return results
    def display(self, a, b, c):
        data = self.generate(a, b, c)
        print("A | B | C | A AND B | A AND C | B AND C | A AND B AND C")
        print("-" * 55)
        for (a_val, b_val, c_val), truth_value in data:
            ab = a_val and b_val
            ac = a_val and c_val
            bc = b_val and c_val
            abc = a_val and b_val and c_val
            print(f"{a_val} | {b_val} | {c_val} | {ab} | {ac} | {bc} | {abc}")
if __name__ == '__main__':
    generator = TruthTableGenerator()
    generator.display(0, 0, 0)
    print("\n" + "="*55 + "\n")
    generator.display(0, 0, 1)
    print("\n" + "="*55 + "\n")
    generator.display(0, 1, 0)
    print("\n" + "="*55 + "\n")
    generator.display(1, 0, 0)
    print("\n" + "="*55 + "\n")
    generator.display(1, 1, 0)
    print("\n" + "="*55 + "\n")
    generator.display(1, 0, 1)
    print("\n" + "="*55 + "\n")
    generator.display(0, 1, 1)
    print("\n" + "="*55 + "\n")
    generator.display(1, 1, 1)