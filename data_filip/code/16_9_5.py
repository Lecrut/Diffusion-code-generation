import math
from typing import List, Tuple

def compress_rle_float(data: List[float], epsilon: float = 1e-9) -> List[Tuple[float, int]]:
    if not data:
        return []
    
    compressed = []
    current_val = data[0]
    count = 1
    
    for i in range(1, len(data)):
        val = data[i]
        if math.isclose(val, current_val, rel_tol=epsilon, abs_tol=epsilon):
            count += 1
        else:
            compressed.append((current_val, count))
            current_val = val
            count = 1
            
    compressed.append((current_val, count))
    return compressed

def decompress_rle_float(compressed: List[Tuple[float, int]]) -> List[float]:
    decompressed = []
    for val, count in compressed:
        for _ in range(count):
            decompressed.append(val)
    return decompressed

if __name__ == '__main__':
    sample_data = [1.0, 1.0, 1.0, 1.0, 2.0, 2.0, 3.0, 3.0, 3.0, 3.0, 3.0, 4.0]
    compressed = compress_rle_float(sample_data)
    print(compressed)
    decompressed = decompress_rle_float(compressed)
    print(decompressed)