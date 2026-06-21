class TruthTableGenerator:
    def generate(self):
        table = []
        for a in [0, 1]:
            for b in [0, 1]:
                table.append((a, b))
        return table

if __name__ == '__main__':
    generator = TruthTableGenerator()
    result = generator.generate()
    print(result)