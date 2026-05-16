class TruthTableGenerator:
    def generate(self, a, b, c):
        results = []
        for i in range(8):
            a_val = (i >> 2) & 1
            b_val = (i >> 1) & 1
            c_val = i & 1
            a_str = str(a_val)
            b_str = str(b_val)
            c_str = str(c_val)
            row = [a_str, b_str, c_str]
            if a_val == 1:
                row.append(str(a_val))
            else:
                row.append(str(a_val))
            if b_val == 1:
                row.append(str(b_val))
            else:
                row.append(str(b_val))
            if c_val == 1:
                row.append(str(c_val))
            else:
                row.append(str(c_val))
            results.append(row)
        return results
    def display(self, results):
        headers = ["A", "B", "C"]
        print(f"{headers[0]:<3} {headers[1]:<3} {headers[2]:<3} |")
        print("-" * 15)
        for row in results:
            print(f"{row[0]:<3} {row[1]:<3} {row[2]:<3} |")
if __name__ == '__main__':
    generator = TruthTableGenerator()
    a_sample = 0
    b_sample = 1
    c_sample = 0
    print("Generating truth table for A, B, C with sample values A=0, B=1, C=0")
    table_data = generator.generate(a_sample, b_sample, c_sample)
    generator.display(table_data)
    print("\nGenerating truth table for A, B, C with sample values A=1, B=0, C=1")
    table_data_2 = generator.generate(1, 0, 1)
    generator.display(table_data_2)