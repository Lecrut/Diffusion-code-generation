from typing import Iterable

class ScoreCalculator:
    def compute_average(self, scores: Iterable[float]) -> float:
        return sum(scores) / len(scores)

if __name__ == '__main__':
    calculator = ScoreCalculator()
    sample_scores1 = [85, 92, 78, 88]
    average1 = calculator.compute_average(sample_scores1)
    print(f"Average of {sample_scores1}: {average1}")
    
    sample_scores2 = [10, 20, 30, 40, 50]
    average2 = calculator.compute_average(sample_scores2)
    print(f"Average of {sample_scores2}: {average2}")
    
    sample_scores3 = []
    average3 = calculator.compute_average(sample_scores3)
    print(f"Average of {sample_scores3}: {average3}")