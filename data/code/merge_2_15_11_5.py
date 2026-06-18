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
    sample_data = [3, 1.5, '2', -4, 0, None]
    try:
        valid_numbers = []
        for item in sample_data:
            if isinstance(item, (int, float)) and not isinstance(item, bool):
                valid_numbers.append(float(item) if isinstance(item, str) else item)
        result = sort_mixed_sequence(valid_numbers)
        print(result)
    except Exception as e:
        print(f"Error occurred: {e}")