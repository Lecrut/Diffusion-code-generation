class GrowingSequence:
    def __init__(self):
        self.current_value = 2

    def next_term(self):
        result = round(self.current_value)
        self.current_value *= 1.5
        return result

if __name__ == '__main__':
    sequence = GrowingSequence()
    for _ in range(6):
        print(sequence.next_term())