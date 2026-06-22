from typing import Iterable

class ScoreCalculator:
    def compute_average(self, scores: Iterable[float]) -> float:
        if not scores:
            return 0
        return sum(scores) / len(scores)

if __name__ == '__main__':
    calculator = ScoreCalculator()
    sample_scores1 = [85, 92, 78, 88]
    avg1 = calculator.compute_average(sample_scores1)
    print(f"Average of {sample_scores1}: {avg1}")
    
    sample_scores2 = [10, 20, 30, 40, 50]
    avg2 = calculator.compute_average(sample_scores2)
    print(f"Average of {sample_scores2}: {avg2}")
    
    sample_scores3 = []
    avg3 = calculator.compute_average(sample_scores3)
    print(f"Average of {sample_scores3}: {avg3}")