class NumberGenerator:
    def generate_odd_numbers(self):
        return list(range(1, 101, 2))

if __name__ == '__main__':
    generator = NumberGenerator()
    odd_numbers = generator.generate_odd_numbers()
    print(odd_numbers)