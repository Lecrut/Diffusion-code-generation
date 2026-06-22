def validate_sequence(sequence: list[int]) -> bool:
    if not isinstance(sequence, list):
        return False
    for item in sequence:
        if not isinstance(item, int):
            return False
    return True

def calculate_sum(sequence: list[int]) -> int:
    if not validate_sequence(sequence):
        raise ValueError("Invalid sequence. Expected a list of integers.")
    
    total = 0
    for number in sequence:
        total += number
    return total

if __name__ == '__main__':
    data = [1, 2, 3, 4, 5]
    result = calculate_sum(data)
    print(result)