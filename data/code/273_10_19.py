class SequenceExecutor:
    GREETING = 'Hello'
    ADDITION_RESULT = 2 + 3
    MULTIPLICATION_CONSTANT = 4

    @staticmethod
    def execute_sequence():
        return SequenceExecutor.GREETING, (SequenceExecutor.ADDITION_RESULT * SequenceExecutor.MULTIPLICATION_CONSTANT)

if __name__ == '__main__':
    executor = SequenceExecutor()
    for _ in range(3):
        greeting, result = executor.execute_sequence()
        print(greeting)
        print(result)