from dataclasses import dataclass

@dataclass
class LogicInput:
    X: bool
    Y: bool
    Z: bool
    W: bool

def evaluate_logic_expression(X: bool, Y: bool, Z: bool, W: bool) -> bool:
    if not all(isinstance(val, bool) for val in [X, Y, Z, W]):
        raise ValueError("All inputs must be boolean type")
    left_term = X and Y
    right_term = Z and (not W)
    return left_term or right_term

if __name__ == '__main__':
    inputs = LogicInput(X=True, Y=False, Z=True, W=True)
    result = evaluate_logic_expression(inputs.X, inputs.Y, inputs.Z, inputs.W)
    print(result)