class SequenceExecutor:
    def execute(self):
        print('Hello')
        result = (2 + 3) * 4
        return result

if __name__ == '__main__':
    executor = SequenceExecutor()
    for _ in range(3):
        print(executor.execute())