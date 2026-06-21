from typing import List

def calculate_total(numbers: List[int]) -> int:
    return sum(numbers)

if __name__ == '__main__':
    sample1 = [1, 2, 3, 4, 5]
    print(f"Total of {sample1}: {calculate_total(sample1)}")
    
    sample2 = [10, -5, 20, 0]
    print(f"Total of {sample2}: {calculate_total(sample2)}")
    
    sample3 = []
    print(f"Total of {sample3}: {calculate_total(sample3)}")
    
    sample4 = [100]
    print(f"Total of {sample4}: {calculate_total(sample4)}")