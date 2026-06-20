class OperationEvaluator:
    @staticmethod
    def is_permitted(data_valid: bool, source_ok: bool) -> bool:
        return data_valid and source_ok

if __name__ == '__main__':
    result1 = OperationEvaluator.is_permitted(True, True)
    print(f"is_permitted(True, True): {result1}")
    result2 = OperationEvaluator.is_permitted(False, False)
    print(f"is_permitted(False, False): {result2}")