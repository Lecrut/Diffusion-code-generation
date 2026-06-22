from itertools import groupby
from typing import Iterator, Tuple, Any, Union

def run_length_encode(data: Union[str, list]) -> Iterator[Tuple[Any, int]]:
    return ((char, len(list(group))) for char, group in groupby(data))

def run_length_decode(encoded_data: Iterator[Tuple[Any, int]]) -> list:
    decoded_list = []
    for char, count in encoded_data:
        decoded_list.extend([char] * count)
    return decoded_list
if __name__ == '__main__':
    sample_string = 'aaabbc'
    encoded = list(run_length_encode(sample_string))
    print(encoded)
    decoded = run_length_decode(iter(encoded))
    print(''.join(decoded))