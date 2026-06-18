import numpy as np
def check_evenness_fast(values: list[int]) -> dict[str, bool]:
    results = {val: (not val & 1) for val in values}
    return results
if __name__ == '__main__':
    sample_data = [2, -4, 0, 3, 7]
    output = check_evenness_fast(sample_data)
    print(output)