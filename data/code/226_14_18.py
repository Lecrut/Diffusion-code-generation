from typing import List

class SequenceRepeater:
    def __init__(self, base_sequence: str):
        self.base_sequence = base_sequence

    def repeat(self, k: int) -> str:
        return self.base_sequence * k

if __name__ == '__main__':
    sample_sequence = 'ABC'
    repetitions = 5
    repeater_instance = SequenceRepeater(sample_sequence)
    result = repeater_instance.repeat(repetitions)
    print(result)