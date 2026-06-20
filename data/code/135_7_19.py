import types

class LambdaEquivalenceChecker:
    @staticmethod
    def get_bytecode(func):
        return func.__code__.co_code

    @staticmethod
    def evaluate_lambda(lambda_func, *args):
        return lambda_func(*args)

    @staticmethod
    def check_equivalence(lambda1, lambda2, *sample_args):
        bytecode1 = LambdaEquivalenceChecker.get_bytecode(lambda1)
        bytecode2 = LambdaEquivalenceChecker.get_bytecode(lambda2)

        if bytecode1 != bytecode2:
            return False

        result1 = LambdaEquivalenceChecker.evaluate_lambda(lambda1, *sample_args)
        result2 = LambdaEquivalenceChecker.evaluate_lambda(lambda2, *sample_args)

        return result1 == result2

if __name__ == '__main__':
    lambda1 = lambda x: x + 1
    lambda2 = lambda y: y + 1
    sample_args = (5,)
    
    print(LambdaEquivalenceChecker.check_equivalence(lambda1, lambda2, *sample_args))