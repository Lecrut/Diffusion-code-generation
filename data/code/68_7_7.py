from typing import List

def calculate_differences(A: List[float], B: List[float]) -> List[float]:
    differences = []
    for a in A:
        for b in B:
            difference = abs(a - b)
            differences.append(difference)
    return differences

if __name__ == '__main__':
    list_A = [2.5, 7.3, 11.8]
    list_B = [4.6, 9.1, 13.4]
    result_differences = calculate_differences(list_A, list_B)
    print(result_differences)