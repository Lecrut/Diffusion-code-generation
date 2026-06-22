from itertools import groupby
from typing import List, Tuple

CHAR = str
COUNT = int
ENCODING_PAIR = Tuple[COUNT, CHAR]
RESULT_TYPE = str

def _compress_groups(pairs: List[ENCODING_PAIR]) -> RESULT_TYPE:
    segments = []
    for count, char in pairs:
        if count == 1:
            segments.append(char)
        else:
            segments.append(f"{count}{char}")
    return "".join(segments)

def run_length_encode(input_string: str) -> RESULT_TYPE:
    if not input_string:
        return ""
    grouped_data = groupby(input_string)
    compressed_pairs = [(len(list(group)), key) for key, group in grouped_data]
    return _compress_groups(compressed_pairs)

if __name__ == '__main__':
    test_data = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"
    output = run_length_encode(test_data)
    print(output)