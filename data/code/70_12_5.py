from typing import List, Tuple

def get_boundary_values(data: List[int]) -> Tuple[int, int]:
    if len(data) == 0:
        raise ValueError("List must not be empty")
    return data[0], data[-1]

if __name__ == '__main__':
    sample_data: List[int] = [5, 15, 25, 35, 45]
    first_val, last_val = get_boundary_values(sample_data)
    print(first_val, last_val)