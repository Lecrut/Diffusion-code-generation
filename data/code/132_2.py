class BooleanLogic:
    def evaluate_xor(self, a, b):
        return a ^ b
if __name__ == '__main__':
    logic = BooleanLogic()
    result1 = logic.evaluate_xor(True, False)
    print(f"XOR(True, False): {result1}")
    result2 = logic.evaluate_xor(True, True)
    print(f"XOR(True, True): {result2}")
    result3 = logic.evaluate_xor(False, True)
    print(f"XOR(False, True): {result3}")
    result4 = logic.evaluate_xor(False, False)
    print(f"XOR(False, False): {result4}")