def repeat_instructions(instructions, count):
    result = []
    for instruction in instructions:
        result.extend([instruction] * count)
    return result
if __name__ == '__main__':
    sample_instructions = ["A", "B", "C"]
    repetition_count = 3
    repeated_list = repeat_instructions(sample_instructions, repetition_count)
    print(repeated_list)