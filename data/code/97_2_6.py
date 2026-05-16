class TruthTableGenerator:
    def generate(self, a, b, c):
        results = []
        for val_a in [0, 1]:
            for val_b in [0, 1]:
                for val_c in [0, 1]:
                    result = (val_a, val_b, val_c)
                    truth_value = str(val_a) + str(val_b) + str(val_c)
                    results.append((result, truth_value))
        return results
    def display(self, results):
        headers = ["A", "B", "C", "A AND B", "A OR B", "A XOR B", "A AND C", "A OR C", "A XOR C", "B AND C", "B OR C", "B XOR C", "C"]
        print(f"{'A':<3}{'B':<3}{'C':<3} | {'A AND B':<8} {'A OR B':<8} {'A XOR B':<8} | {'A AND C':<8} {'A OR C':<8} {'A XOR C':<8} | {'B AND C':<8} {'B OR C':<8} {'B XOR C':<8} | {'C':<3}")
        print("-" * 75)
        for (a, b, c), truth_value in results:
            ab = a & b
            ac = a & c
            bc = b & c
            and_ab = a & b
            or_ab = a | b
            xor_ab = a ^ b
            and_ac = a & c
            or_ac = a | c
            xor_ac = a ^ c
            and_bc = b & c
            or_bc = b | c
            xor_bc = b ^ c
            print(f"{a:<3}{b:<3}{c:<3} | {ab:<8} {or_ab:<8} {xor_ab:<8} | {and_ac:<8} {or_ac:<8} {xor_ac:<8} | {and_bc:<8} {or_bc:<8} {xor_bc:<8} | {c:<3}")
if __name__ == '__main__':
    generator = TruthTableGenerator()
    a_val = 0
    b_val = 1
    c_val = 0
    all_results = generator.generate(a_val, b_val, c_val)
    generator.display(all_results)