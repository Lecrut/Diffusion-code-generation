from typing import List, Tuple, Any

VALIDATION_BOUNDS: Tuple[str, str] = ("negative_index", "exceeds_length")
COMPARISON_SYMBOLS: Tuple[str, str, str] = ("<", ">", "==")

def compare_data_pairs(data: List[Any], indices: List[int]) -> List[str]:
    if not data:
        return []
    if not indices:
        return []
    
    data_len = len(data)
    results: List[str] = []
    
    for i in range(0, len(indices) - 1, 2):
        idx_a = indices[i]
        idx_b = indices[i + 1]
        
        if idx_a < 0 or idx_a >= data_len:
            raise ValueError(f"Index {idx_a} is invalid for data of length {data_len}")
        if idx_b < 0 or idx_b >= data_len:
            raise ValueError(f"Index {idx_b} is invalid for data of length {data_len}")
            
        val_a = data[idx_a]
        val_b = data[idx_b]
        
        if val_a < val_b:
            results.append(f"{val_a} {COMPARISON_SYMBOLS[0]} {val_b}")
        elif val_a > val_b:
            results.append(f"{val_a} {COMPARISON_SYMBOLS[1]} {val_b}")
        else:
            results.append(f"{val_a} {COMPARISON_SYMBOLS[2]} {val_b}")
            
    return results

if __name__ == '__main__':
    sample_values = [100, 200, 150, 250, 300, 50]
    sample_indices = [0, 5, 1, 2]
    output = compare_data_pairs(sample_values, sample_indices)
    print(output)