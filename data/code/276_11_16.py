def repeat_instructions(instructions, count):
    if not instructions:
        return []
    
    if not isinstance(count, int) or count < 0:
        raise ValueError("Count must be a non-negative integer")
    
    result = []
    for instruction in instructions:
        if isinstance(instruction, str):
            result.extend([instruction] * count)
        else:
            raise ValueError("Instructions must be strings")
    
    return result

if __name__ == '__main__':
    sample_instructions = ["step 1", "step 2", "step 3"]
    repetition_count = 3
    repeated_list = repeat_instructions(sample_instructions, repetition_count)
    print(repeated_list)