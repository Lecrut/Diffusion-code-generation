class EvenNumberGenerator:
    def generate_even_numbers(self, start_value, length):
        sequence = []
        current_value = start_value
        for _ in range(length):
            if current_value % 2 == 0:
                sequence.append(current_value)
            else:
                continue
            current_value += 1
        return sequence

if __name__ == '__main__':
    generator = EvenNumberGenerator()
    start = 2
    length = 10
    result = generator.generate_even_numbers(start, length)
    print(result)