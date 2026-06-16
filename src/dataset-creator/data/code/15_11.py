from typing import List, Union
def sort_mixed_sequence(sequence: List[Union[int, float]]) -> List[Union[int, float]]:
    if not sequence:
        return []
    try:
        sorted_seq = sorted(sequence)
        return sorted_seq
    except TypeError:
        raise ValueError("List must contain only numeric types.")
if __name__ == '__main__':
    sample_data = [3, 1.5, '2', -4, None]                                                            
    try:
        result = sort_mixed_sequence(sample_data)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")