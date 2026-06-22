from dataclasses import dataclass

@dataclass(frozen=True)
class InequalityRecord:
    index: int
    left_value: object
    right_value: object

PAIR_OFFSET: int = 1

def detect_adjacent_inequalities(input_sequence: list) -> list:
    sequence_length: int = len(input_sequence)
    threshold: int = sequence_length - PAIR_OFFSET
    findings: list = []
    
    if threshold < 0:
        return findings
    
    current_index: int = 0
    while current_index < threshold:
        left_item: object = input_sequence[current_index]
        right_item: object = input_sequence[current_index + 1]
        
        if left_item != right_item:
            findings.append(InequalityRecord(current_index, left_item, right_item))
            
        current_index += 1
        
    return findings

if __name__ == '__main__':
    test_data: list = [10, 10, 20, 20, 30, 25, 40, 40, 50, 55]
    result: list = detect_adjacent_inequalities(test_data)
    print(result)