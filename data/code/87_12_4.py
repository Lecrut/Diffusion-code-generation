class OperationEvaluator:
    @staticmethod
    def is_operation_permitted(data_valid: bool, source_ok: bool) -> bool:
        return data_valid and source_ok

if __name__ == '__main__':
    print(OperationEvaluator.is_operation_permitted(True, True))
    print(OperationEvaluator.is_operation_permitted(False, False))