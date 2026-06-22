class FibonacciSequence:
    MAX_LIMIT = 10

    @staticmethod
    def generate_sequence(limit):
        if limit <= 0:
            return []
        elif limit == 1:
            return [1]
        
        sequence = [1, 2]
        while len(sequence) < limit:
            next_value = sequence[-1] + sequence[-2]
            sequence.append(next_value)
        return sequence[:limit]

if __name__ == '__main__':
    result = FibonacciSequence.generate_sequence(FibonacciSequence.MAX_LIMIT)
    print(*result)