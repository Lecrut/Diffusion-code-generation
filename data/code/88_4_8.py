class LogicalOperator:
    @staticmethod
    def and_operation(val1: bool, val2: bool) -> bool:
        return val1 and val2

if __name__ == '__main__':
    operator = LogicalOperator()
    print(f"True AND True = {operator.and_operation(True, True)}")
    print(f"True AND False = {operator.and_operation(True, False)}")
    print(f"False AND True = {operator.and_operation(False, True)}")
    print(f"False AND False = {operator.and_operation(False, False)}")