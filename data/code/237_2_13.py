class PowerOfTwoGenerator:
    def generate_powers_of_two(self, n):
        powers = []
        for i in range(n):
            power = 1 << i
            powers.append(power)
        return powers

if __name__ == '__main__':
    generator = PowerOfTwoGenerator()
    number_of_powers = 10
    result = generator.generate_powers_of_two(number_of_powers)
    print(result)