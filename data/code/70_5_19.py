class EndpointEvaluator:
    MIN_LENGTH = 2

    def __init__(self, sequence):
        self._sequence = sequence

    def evaluate_extremities(self):
        if len(self._sequence) < self.MIN_LENGTH:
            raise ValueError(f"Sequence length {len(self._sequence)} is below minimum {self.MIN_LENGTH}")
        return (self._sequence[0], self._sequence[-1])

if __name__ == '__main__':
    evaluator = EndpointEvaluator([99, 100, 101])
    print(evaluator.evaluate_extremities())
    try:
        evaluator_short = EndpointEvaluator([1])
        evaluator_short.evaluate_extremities()
    except ValueError as e:
        print(f"Caught error: {e}")