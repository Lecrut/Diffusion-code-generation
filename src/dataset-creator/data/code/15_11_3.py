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
        clean_sequence = []
        for item in sample_data:
            if isinstance(item, (int, float)) and not isinstance(item, bool):
                clean_sequence.append(float(item) if isinstance(item, str) else item)
        result = sort_mixed_sequence(clean_sequence)
        print(result)
    except ValueError as ve:
        print(f"Error processing data: {ve}")