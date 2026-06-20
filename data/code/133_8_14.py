class LogicalEvaluator:
    TRUE = True
    FALSE = False
    
    def __iter__(self):
        yield self.TRUE and self.FALSE
        yield 1 == 1
        yield not (3 > 2)
        yield "hello" in "hello world"
        yield len([1, 2, 3]) == 3

if __name__ == '__main__':
    evaluator = LogicalEvaluator()
    for result in evaluator:
        print(result)