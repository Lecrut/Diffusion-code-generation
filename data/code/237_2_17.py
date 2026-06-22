class PowerOfTwoGenerator:
    @staticmethod
    def generate_powers_of_two(n):
        powers = []
        for i in range(n):
            power = 1 << i
            powers.append(power)
        return powers

if __name__ == '__main__':
    generator = PowerOfTwoGenerator()
    result = generator.generate_powers_of_two(10)
    print(result)