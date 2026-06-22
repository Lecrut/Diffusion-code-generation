def repeat_instructions(instructions, times):
    if not instructions or not all(isinstance(t, int) for t in times):
        return []
    
    result = []
    for instruction, time in zip(instructions, times):
        result.extend([instruction] * time)
    
    return result

if __name__ == '__main__':
    sample_instructions = ["Move forward", "Turn right"]
    sample_times = [2, 3]
    print(repeat_instructions(sample_instructions, sample_times))