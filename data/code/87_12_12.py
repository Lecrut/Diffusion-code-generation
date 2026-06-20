class OperationEvaluator:
    @staticmethod
    def evaluate_flags(data_valid: bool, source_ok: bool) -> bool:
        return data_valid and source_ok

if __name__ == '__main__':
    sample1 = OperationEvaluator.evaluate_flags(True, True)
    print(f"OperationEvaluator.evaluate_flags(True, True): {sample1}")
    sample2 = OperationEvaluator.evaluate_flags(False, False)
    print(f"OperationEvaluator.evaluate_flags(False, False): {sample2}")