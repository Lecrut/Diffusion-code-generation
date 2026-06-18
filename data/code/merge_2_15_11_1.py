from typing import List, Union
def sort_mixed_sequence(sequence: List[Union[int, float]]) -> List[Union[int, float]]:
    if not sequence:
        return []
    sorted_list = sorted(sequence)
    return sorted_list
if __name__ == '__main__':
    sample_data = [3.5, 2, -1, '4', 0, None]                                                                                                
    def is_numeric(value):
        return isinstance(value, (int, float)) and not isinstance(value, bool)
    filtered_data = [x for x in sample_data if is_numeric(x)]
    result = sort_mixed_sequence(filtered_data)
    print(result)