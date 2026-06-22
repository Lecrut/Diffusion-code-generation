class RepeatingSequence:
    def __init__(self, base_sequence: str):
        self.base_sequence = base_sequence

    def repeat(self, k: int) -> str:
        return self.base_sequence * k

if __name__ == '__main__':
    seq_instance = RepeatingSequence('X')
    print(seq_instance.repeat(3))