from typing import List

def calculate_differences(A: List[float], B: List[float]) -> List[float]:
    differences = []
    for a in A:
        for b in B:
            difference = abs(a - b)
            differences.append(difference)
    return differences

if __name__ == '__main__':
    A_sample = [1.5, 3.2, 7.8]
    B_sample = [2.4, 5.6, 9.0]
    result = calculate_differences(A_sample, B_sample)
    print(result)