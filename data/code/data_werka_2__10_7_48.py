class TemperatureEvaluator:
    TOLERANCE = 1

    @staticmethod
    def evaluate_difference(temp1, temp2):
        if not isinstance(temp1, (int, float)) or not isinstance(temp2, (int, float)):
            raise ValueError("Both temperature values must be numbers.")
        return abs(temp1 - temp2) <= TemperatureEvaluator.TOLERANCE

if __name__ == '__main__':
    sample_temp1 = 22.0
    sample_temp2 = 23.5
    evaluator = TemperatureEvaluator()
    result = evaluator.evaluate_difference(sample_temp1, sample_temp2)
    print(result)