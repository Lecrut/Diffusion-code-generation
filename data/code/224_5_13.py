class ScoreCalculator:
    def __init__(self, scores):
        self.scores = iter(scores)

    def calculate_mean(self):
        running_total = 0
        count = 0
        for score in self.scores:
            running_total += score
            count += 1
        return running_total / count

if __name__ == '__main__':
    calculator = ScoreCalculator([10, 20, 30, 40, 50])
    mean = calculator.calculate_mean()
    print(f"The mean of the scores is: {mean}")