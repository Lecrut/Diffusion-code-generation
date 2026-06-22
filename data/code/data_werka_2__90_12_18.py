from typing import Tuple

class OrLogicGate:
    def __init__(self, left: bool, right: bool):
        self.left = left
        self.right = right

    def evaluate(self) -> bool:
        left_bit = 1 if self.left else 0
        right_bit = 1 if self.right else 0
        return bool(left_bit | right_bit)

    def get_state(self) -> Tuple[bool, bool, bool]:
        return (self.left, self.right, self.evaluate())

def check_or_condition(a: bool, b: bool) -> bool:
    gate = OrLogicGate(a, b)
    return gate.evaluate()

if __name__ == '__main__':
    gate1 = OrLogicGate(True, False)
    print(gate1.evaluate())
    print(gate1.get_state())
    result = check_or_condition(False, True)
    print(result)