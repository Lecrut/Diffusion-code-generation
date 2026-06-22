def repeat_instructions(instructions, count):
    if not instructions:
        raise ValueError("Instructions list cannot be empty.")
    if not isinstance(count, int) or count < 1:
        raise ValueError("Count must be a positive integer.")
    
    result = []
    for instruction in instructions:
        result.extend([instruction] * count)
    return result

if __name__ == '__main__':
    sample_instructions = ["step 1", "step 2", "step 3"]
    repetition_count = 3
    repeated_list = repeat_instructions(sample_instructions, repetition_count)
    print(repeated_list)