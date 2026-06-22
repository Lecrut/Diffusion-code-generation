class TruthTableGenerator:
    def generate(self):
        return [
            (False, False),
            (False, True),
            (True, False),
            (True, True)
        ]

if __name__ == '__main__':
    generator = TruthTableGenerator()
    result = generator.generate()
    print(result)