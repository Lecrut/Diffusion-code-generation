def repeat_instructions(instructions, count):
    if not instructions or not isinstance(count, int) or count < 0:
        return []
    
    repeated = []
    for instruction in instructions:
        repeated.extend([instruction] * count)
    
    return repeated

if __name__ == '__main__':
    sample_instructions = ['jump', 'run', 'stop']
    repeat_count = 3
    result = repeat_instructions(sample_instructions, repeat_count)
    print(result)