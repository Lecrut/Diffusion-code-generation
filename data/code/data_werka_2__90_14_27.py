def evaluate_logical_or(left_operand, right_operand):
    if left_operand is None:
        raise ValueError("Left operand cannot be None")
    if right_operand is None:
        raise ValueError("Right operand cannot be None")
    if not isinstance(left_operand, (bool, int, float, str, list, tuple, dict, set)):
        raise ValueError("Left operand type not supported")
    if not isinstance(right_operand, (bool, int, float, str, list, tuple, dict, set)):
        raise ValueError("Right operand type not supported")
    return left_operand or right_operand

class OrConditionTester:
    def __init__(self):
        self.results = []

    def run_test(self, a, b):
        value = evaluate_logical_or(a, b)
        self.results.append((a, b, value))
        return value

if __name__ == '__main__':
    tester = OrConditionTester()
    val1 = tester.run_test(0, 1)
    print(val1)
    val2 = tester.run_test(False, "success")
    print(val2)
    val3 = tester.run_test([], [1, 2, 3])
    print(val3)
    val4 = tester.run_test("", "default")
    print(val4)
    val5 = tester.run_test(0, 0)
    print(val5)
    val6 = tester.run_test(None, None)
    print(val6)
    val7 = tester.run_test(10, 20)
    print(val7)
    val8 = tester.run_test("", "")
    print(val8)
    val9 = tester.run_test(0.0, 0.1)
    print(val9)
    val10 = tester.run_test((), [1])
    print(val10)
    val11 = tester.run_test({}, {"key": "value"})
    print(val11)
    val12 = tester.run_test(0, "")
    print(val12)
    val13 = tester.run_test(False, False)
    print(val13)
    val14 = tester.run_test(0, False)
    print(val14)
    val15 = tester.run_test(0, None)
    print(val15)
    val16 = tester.run_test(None, 0)
    print(val16)
    val17 = tester.run_test(0, 0.0)
    print(val17)
    val18 = tester.run_test(0, "")
    print(val18)
    val19 = tester.run_test(0, False)
    print(val19)
    val20 = tester.run_test(0, None)
    print(val20)