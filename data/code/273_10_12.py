class SequenceExecutor:
    GREETING = 'Hello'
    
    @staticmethod
    def calculate():
        addition_result = 2 + 3
        multiplication_result = addition_result * 4
        return multiplication_result

if __name__ == '__main__':
    executor = SequenceExecutor()
    for _ in range(3):
        print(executor.GREETING)
        print(executor.calculate())