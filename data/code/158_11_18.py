class EvenNumberGenerator:
    START = 2
    END = 100
    
    def generate_evens(self):
        for num in range(EvenNumberGenerator.START, EvenNumberGenerator.END + 1):
            if num % 2 == 0:
                yield num

if __name__ == '__main__':
    generator = EvenNumberGenerator()
    print(list(generator.generate_evens()))