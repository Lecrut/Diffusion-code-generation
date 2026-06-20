class TruthTableGenerator:
    def generate_truth_table(self):
        print(f"A | B | A AND B | A OR B | A XOR B | NOT A | NOT B")
        for a in [True, False]:
            for b in [True, False]:
                and_result = a and b
                or_result = a or b
                xor_result = a != b
                not_a = not a
                not_b = not b
                print(f"{a} | {b} | {and_result} | {or_result} | {xor_result} | {not_a} | {not_b}")

if __name__ == '__main__':
    generator = TruthTableGenerator()
    generator.generate_truth_table()