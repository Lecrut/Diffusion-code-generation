import itertools
from typing import List, Tuple, Union

def run_length_encode(data: Union[str, List]) -> List[Tuple[Union[str, int], int]]:
    if not data:
        return []
    
    def group_iterator():
        for key, group in itertools.groupby(data):
            count = sum(1 for _ in group)
            yield key, count
    
    return list(group_iterator())

def run_length_decode(encoded_data: List[Tuple[Union[str, int], int]]) -> Union[str, List]:
    if not encoded_data:
        return []
    
    if isinstance(encoded_data[0][0], str):
        return "".join(key * count for key, count in encoded_data)
    
    result = []
    for key, count in encoded_data:
        result.extend([key] * count)
    return result

if __name__ == '__main__':
    sample_string = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"
    encoded_result = run_length_encode(sample_string)
    print(encoded_result)
    
    decoded_result = run_length_decode(encoded_result)
    print(decoded_result)
    
    sample_list = [1, 1, 1, 2, 2, 3, 3, 3, 3]
    encoded_list_result = run_length_encode(sample_list)
    print(encoded_list_result)
    
    decoded_list_result = run_length_decode(encoded_list_result)
    print(decoded_list_result)