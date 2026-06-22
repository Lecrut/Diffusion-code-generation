def repeat_instructions(instructions, times):
    if not instructions or not all(isinstance(t, int) for t in times):
        return []
    return [inst * time for inst, time in zip(instructions, times)]

if __name__ == '__main__':
    sample_instructions = ["Jump", "Run"]
    sample_times = [3, 2]
    print(repeat_instructions(sample_instructions, sample_times))