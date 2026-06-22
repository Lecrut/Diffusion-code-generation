from typing import Iterable

class ScoreCalculator:
    def calculate_mean(self, scores: Iterable[float]) -> float:
        if not scores:
            return 0
        total = sum(scores)
        count = len(scores)
        return total / count

if __name__ == '__main__':
    calculator = ScoreCalculator()
    sample_scores1 = [85.5, 90.0, 78.2, 92.1]
    mean1 = calculator.calculate_mean(sample_scores1)
    print(f"Mean of {sample_scores1}: {mean1}")
    
    sample_scores2 = [10, 20, 30, 40, 50]
    mean2 = calculator.calculate_mean(sample_scores2)
    print(f"Mean of {sample_scores2}: {mean2}")
    
    sample_scores3 = []
    mean3 = calculator.calculate_mean(sample_scores3)
    print(f"Mean of {sample_scores3}: {mean3}")