import statistics
from typing import List, Union

ScoreType = Union[int, float]

class TestScoreAnalyzer:
    def __init__(self, scores: List[ScoreType]) -> None:
        if not isinstance(scores, list):
            raise TypeError("Scores must be provided as a list.")
        if len(scores) == 0:
            raise ValueError("The list of scores cannot be empty.")
        for index, value in enumerate(scores):
            if not isinstance(value, (int, float)):
                raise TypeError(f"Invalid score type at index {index}: {type(value).__name__}")
        self._scores = scores

    def get_mean(self) -> float:
        return statistics.mean(self._scores)

    def get_count(self) -> int:
        return len(self._scores)

    def validate(self) -> bool:
        return all(isinstance(s, (int, float)) for s in self._scores)

if __name__ == '__main__':
    sample_data = [95, 88, 76, 92, 84, 91, 79, 88, 93, 85]
    analyzer = TestScoreAnalyzer(sample_data)
    calculated_mean = analyzer.get_mean()
    total_count = analyzer.get_count()
    is_valid = analyzer.validate()
    print(calculated_mean)
    print(total_count)
    print(is_valid)