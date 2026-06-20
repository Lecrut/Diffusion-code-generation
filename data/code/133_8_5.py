class LogicalEvaluator:
    def __iter__(self):
        self.statements = [
            True and False,
            1 == 1,
            not (3 > 2),
            "hello" in "hello world",
            len([1, 2, 3]) == 3
        ]
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self.statements):
            raise StopIteration
        result = self.statements[self.index]
        self.index += 1
        return result

if __name__ == '__main__':
    evaluator = LogicalEvaluator()
    for result in evaluator:
        print(result)