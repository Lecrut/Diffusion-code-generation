class BooleanLogic:
    def evaluate_xor(self, a, b):
        return a ^ b
if __name__ == '__main__':
    logic = BooleanLogic()
    result1 = logic.evaluate_xor(True, False)
    result2 = logic.evaluate_xor(True, True)
    result3 = logic.evaluate_xor(False, True)
    result4 = logic.evaluate_xor(False, False)
    print(f"XOR(True, False): {result1}")
    print(f"XOR(True, True): {result2}")
    print(f"XOR(False, True): {result3}")
    print(f"XOR(False, False): {result4}")