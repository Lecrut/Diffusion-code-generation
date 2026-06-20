class OperationEvaluator:
    @staticmethod
    def is_permitted(data_valid: bool, source_ok: bool) -> bool:
        return data_valid and source_ok

if __name__ == '__main__':
    evaluator = OperationEvaluator()
    print(f"Operation permitted (True, True): {evaluator.is_permitted(True, True)}")
    print(f"Operation permitted (False, True): {evaluator.is_permitted(False, True)}")
    print(f"Operation permitted (True, False): {evaluator.is_permitted(True, False)}")
    print(f"Operation permitted (False, False): {evaluator.is_permitted(False, False)}")