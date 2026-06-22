class FibonacciGenerator:
    START_A = 0
    START_B = 1

    @staticmethod
    def get_next_pair(current_a, current_b):
        next_a = current_b
        next_b = current_a + current_b
        return (next_a, next_b)

    def generate(self, count):
        if count <= 0:
            return []
        if count == 1:
            return [self.START_A]
        
        results = [self.START_A, self.START_B]
        current_a = self.START_A
        current_b = self.START_B
        limit = count - 2
        
        for _ in range(limit):
            current_a, current_b = self.get_next_pair(current_a, current_b)
            results.append(current_a)
        return results

if __name__ == '__main__':
    gen = FibonacciGenerator()
    output = gen.generate(20)
    print(output)