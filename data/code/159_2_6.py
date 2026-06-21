class OddNumberGenerator:
    def generate_odds(self):
        return list(range(1, 101, 2))

if __name__ == '__main__':
    generator = OddNumberGenerator()
    odd_numbers = generator.generate_odds()
    print(odd_numbers)