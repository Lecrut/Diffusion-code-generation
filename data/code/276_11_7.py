def repeat_instructions(instructions, count):
    if not instructions or not isinstance(count, int) or count <= 0:
        return []
    
    result = []
    for instruction in instructions:
        result.extend([instruction] * count)
    
    return result

if __name__ == '__main__':
    sample_instructions = ["step 1", "step 2", "step 3"]
    repetition_count = 3
    repeated_list = repeat_instructions(sample_instructions, repetition_count)
    print(repeated_list)