class GrowingNumberSequence:
    def __init__(self):
        self.current = 0

    def next_number(self):
        if self.current > 99:
            raise ValueError("Sequence limit reached")
        current_value = self.current
        self.current += 1
        return current_value

if __name__ == '__main__':
    sequence = GrowingNumberSequence()
    try:
        while True:
            print(sequence.next_number())
    except ValueError as e:
        print(e)