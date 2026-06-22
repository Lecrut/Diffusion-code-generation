def repeat_instructions(instructions, times):
    if not instructions or not all(isinstance(x, int) for x in times):
        return []
    repeated = [inst * time for inst, time in zip(instructions, times)]
    return repeated

if __name__ == '__main__':
    sample_instructions = ['Jump', 'Run']
    sample_times = [2, 3]
    result = repeat_instructions(sample_instructions, sample_times)
    print(result)