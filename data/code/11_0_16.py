from collections import Counter
from typing import List

REPETITION_THRESHOLD: int = 1

def get_repeated_chars(input_text: str) -> List[str]:
    char_histogram: Counter = Counter(input_text)
    threshold: int = REPETITION_THRESHOLD
    filtered_chars: List[str] = [
        character
        for character, frequency in char_histogram.items()
        if frequency > threshold
    ]
    return filtered_chars

if __name__ == '__main__':
    test_input: str = "banana"
    output: List[str] = get_repeated_chars(test_input)
    print(output)