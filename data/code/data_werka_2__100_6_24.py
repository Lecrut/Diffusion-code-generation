from functools import reduce
from operator import and_

VALID_CHARS = frozenset('01')

def validate_sequence(bits_str):
    if not isinstance(bits_str, str):
        raise ValueError("Input must be a string")
    if len(bits_str) < 2:
        raise ValueError("Sequence length must be at least 2")
    if not all(c in VALID_CHARS for c in bits_str):
        raise ValueError("Sequence contains invalid characters")
    return list(bits_str)

def evaluate_and_logic(bits_str):
    cleaned_bits = validate_sequence(bits_str)
    operand_bits = cleaned_bits[:-1]
    predicted_result_bit = cleaned_bits[-1]
    
    if not operand_bits:
        raise ValueError("No operands provided for calculation")
    
    logical_values = [bit == '1' for bit in operand_bits]
    actual_result_logical = reduce(and_, logical_values, True)
    
    expected_result_logical = actual_result_logical
    return predicted_result_bit == '1' if expected_result_logical else predicted_result_bit == '0'

class LogicChecker:
    def __init__(self, sequence):
        self.sequence = sequence

    def verify(self):
        return evaluate_and_logic(self.sequence)

if __name__ == '__main__':
    checker = LogicChecker("11110")
    print(checker.verify())
    
    checker2 = LogicChecker("11111")
    print(checker2.verify())