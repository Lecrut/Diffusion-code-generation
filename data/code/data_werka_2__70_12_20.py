from typing import List, Tuple

INDEX_MAP = {
    "first": 0,
    "last": -1
}

def retrieve_boundary_elements(values: List[int]) -> Tuple[int, int]:
    if len(values) == 0:
        raise ValueError("List must not be empty")
    first_idx = INDEX_MAP["first"]
    last_idx = INDEX_MAP["last"]
    first_val = values[first_idx]
    last_val = values[last_idx]
    return (first_val, last_val)

if __name__ == '__main__':
    sample_values: List[int] = [1, 2, 3, 4, 5]
    boundary = retrieve_boundary_elements(sample_values)
    print(boundary)