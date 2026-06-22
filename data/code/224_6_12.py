from typing import List
import math

class StatisticsCalculator:
    @staticmethod
    def calculate_mean(scores: List[float]) -> float:
        return math.fsum(scores) / len(scores)

if __name__ == '__main__':
    sample_scores = [85, 92, 78, 88, 95]
    mean_score = StatisticsCalculator.calculate_mean(sample_scores)
    print(mean_score)