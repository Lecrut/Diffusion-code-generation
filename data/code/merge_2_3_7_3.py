import numpy as np
def is_even_fast(x: int) -> bool:
    return (x & 1) == 0
if __name__ == '__main__':
    samples = [2, -4, 7, 3.5]
    results = []
    for val in samples:
        try:
            if isinstance(val, float):
                continue
            even_check = is_even_fast(int(val))
            results.append(even_check)
        except Exception:
            pass
    print(results)