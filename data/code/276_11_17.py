def repeat_instructions(instructions, repeats):
    if not instructions or not all(isinstance(r, int) for r in repeats):
        return []
    result = []
    for inst, rep in zip(instructions, repeats):
        result.extend([inst] * rep)
    return result

if __name__ == '__main__':
    sample_instructions = ["Jump", "Run"]
    sample_repeats = [2, 3]
    print(repeat_instructions(sample_instructions, sample_repeats))