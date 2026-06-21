class EdgeEvaluator:
    def __init__(self, sequence):
        self.sequence = sequence

    def get_extremities(self):
        if len(self.sequence) < 2:
            raise ValueError("Sequence must have at least two elements")
        return self.sequence[0], self.sequence[-1]

if __name__ == '__main__':
    evaluator = EdgeEvaluator([100, 200, 300, 400, 500])
    print(evaluator.get_extremities())