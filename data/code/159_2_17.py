class OddNumberGenerator:
    def generate(self):
        return list(range(1, 101, 2))

if __name__ == '__main__':
    generator = OddNumberGenerator()
    odd_numbers = generator.generate()
    print(odd_numbers)