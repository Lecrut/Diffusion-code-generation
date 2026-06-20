class LogicEvaluator:
    @staticmethod
    def verify_status(a: bool, b: bool) -> bool:
        return a ^ b

if __name__ == '__main__':
    val1 = True
    val2 = False
    result1 = LogicEvaluator.verify_status(val1, val2)
    print(result1)

    val3 = False
    val4 = True
    result2 = LogicEvaluator.verify_status(val3, val4)
    print(result2)

    val5 = True
    val6 = True
    result3 = LogicEvaluator.verify_status(val5, val6)
    print(result3)

    val7 = False
    val8 = False
    result4 = LogicEvaluator.verify_status(val7, val8)
    print(result4)