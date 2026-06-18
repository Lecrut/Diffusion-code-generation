def generate_sequence(start_value: int = 10, step_size: int = 5) -> list[int]:
    if not isinstance(start_value, int) or not isinstance(step_size, int):
        raise TypeError("Both arguments must be integers.")
    sequence = []
    current_val = start_value
    while current_val <= 210:
        sequence.append(current_val)
        if step_size != 0:
            current_val += step_size
    return sequence
def find_print_index(sequence: list[int], target_number: int) -> int | None:
    try:
        return sequence.index(target_number)
    except ValueError:
        pass
    return None
def main() -> None:
    START_VAL = 10                                                  
    STEP_SIZE = 5                              
    TARGET_NUMBER = 65                                        
    full_sequence = generate_sequence(start_value=START_VAL, step_size=STEP_SIZE)
    result_index = find_print_index(sequence=full_sequence, target_number=TARGET_NUMBER)
    if result_index is not None:
        print(f"Target number {TARGET_NUMBER} found at print index: {result_index}")
    else:
        print(f"Error: Target number {TARGET_NUMBER} was NOT found in the generated sequence.")
if __name__ == '__main__':
    main()