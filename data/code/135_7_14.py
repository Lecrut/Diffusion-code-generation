import dis

class LambdaEquivalenceChecker:
    SAMPLE_VALUES = [1, 2, 3, 4]
    
    @staticmethod
    def get_bytecode(func):
        return dis.Bytecode(func.__code__)
    
    @staticmethod
    def compare_bytecodes(bytecode1, bytecode2):
        return list(bytecode1) == list(bytecode2)
    
    @staticmethod
    def evaluate_lambda(lambda_func, values):
        results = []
        for value in values:
            results.append(lambda_func(value))
        return results
    
    @classmethod
    def check_equivalence(cls, lambda1, lambda2):
        bytecode1 = cls.get_bytecode(lambda1)
        bytecode2 = cls.get_bytecode(lambda2)
        
        if not cls.compare_bytecodes(bytecode1, bytecode2):
            return False
        
        sample_results1 = cls.evaluate_lambda(lambda1, cls.SAMPLE_VALUES)
        sample_results2 = cls.evaluate_lambda(lambda2, cls.SAMPLE_VALUES)
        
        return sample_results1 == sample_results2

if __name__ == '__main__':
    lambda1 = lambda x: x * 2
    lambda2 = lambda x: x * 2
    
    print(LambdaEquivalenceChecker.check_equivalence(lambda1, lambda2))