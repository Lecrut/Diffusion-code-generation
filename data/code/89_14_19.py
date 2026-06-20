class BooleanOperator:
    @staticmethod
    def and_operation(state1: bool, state2: bool) -> bool:
        return state1 and state2

if __name__ == '__main__':
    operator = BooleanOperator()
    result1 = operator.and_operation(True, False)
    print(f"True AND False: {result1}")
    result2 = operator.and_operation(False, False)
    print(f"False AND False: {result2}")
    result3 = operator.and_operation(True, True)
    print(f"True AND True: {result3}")