from typing import List

def calculate_differences(list1: List[float], list2: List[float]) -> List[float]:
    def subtract_elements(a: float, b: float) -> float:
        return a - b
    
    differences = []
    for i in range(min(len(list1), len(list2))):
        diff = subtract_elements(list1[i], list2[i])
        differences.append(diff)
    
    return differences

if __name__ == '__main__':
    sample_list1 = [5.0, 6.3, 7.8]
    sample_list2 = [2.1, 3.4, 4.9]
    result_differences = calculate_differences(sample_list1, sample_list2)
    print(result_differences)