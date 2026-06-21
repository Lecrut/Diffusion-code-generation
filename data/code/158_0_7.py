class EvenNumberGenerator:
    MAX_VALUE = 50
    
    @staticmethod
    def generate_even_numbers():
        return [x for x in range(1, EvenNumberGenerator.MAX_VALUE + 1) if x % 2 == 0]

if __name__ == '__main__':
    even_numbers = EvenNumberGenerator.generate_even_numbers()
    print(even_numbers)