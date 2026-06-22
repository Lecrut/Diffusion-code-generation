from typing import Iterable

def calculate_average(scores: Iterable[float]) -> float:
    if not scores:
        return 0
    total = sum(scores)
    count = len(scores)
    average = total / count
    return average

if __name__ == '__main__':
    sample_scores1 = [85, 92, 78, 88]
    print(f"Mean of {sample_scores1}: {calculate_average(sample_scores1)}")
    
    sample_scores2 = [10, 20, 30, 40, 50]
    print(f"Mean of {sample_scores2}: {calculate_average(sample_scores2)}")
    
    sample_scores3 = []
    print(f"Mean of {sample_scores3}: {calculate_average(sample_scores3)}")