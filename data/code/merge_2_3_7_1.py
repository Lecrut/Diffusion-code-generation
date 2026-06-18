import numpy as np
def check_evenness_fast(values: list[int]) -> dict[str, bool]:
    results = {i % 2 == 0: False for i in values}
    return results
if __name__ == '__main__':
    sample_data = [10, 37, 48, -5, 99]
    output = check_evenness_fast(sample_data)
    print(output)