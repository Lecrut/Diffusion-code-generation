import math
from typing import List, Tuple
class WeightAnalyzer:
    def __init__(self):
        self.abs_diffs = []
        self.signed_diffs = []
        self.percentage_variances = []
    def analyze(self, weights1: List[float], weights2: List[float]) -> None:
        if len(weights1) != len(weights2):
            raise ValueError("Input lists must have the same length.")
        for w1, w2 in zip(weights1, weights2):
            abs_diff = abs(w1 - w2)
            signed_diff = w1 - w2
            if w2 == 0:
                pct_var = float('inf') if w1 != 0 else 0.0
            else:
                pct_var = (w1 / w2) * 100
            self.abs_diffs.append(abs_diff)
            self.signed_diffs.append(signed_diff)
            self.percentage_variances.append(pct_var)
if __name__ == '__main__':
    analyzer = WeightAnalyzer()
    sample_weights_1 = [10.5, 20.3, 30.7]
    sample_weights_2 = [9.8, 21.1, 31.4]
    analyzer.analyze(sample_weights_1, sample_weights_2)
    print("Absolute Differences:", analyzer.abs_diffs)
    print("Signed Differences:", analyzer.signed_diffs)
    print("Percentage Variances:", [round(x, 2) if not math.isinf(x) else x for x in analyzer.percentage_variances])