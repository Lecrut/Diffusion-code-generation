def repeat_instructions(instructions, count):
    return instructions * count
if __name__ == '__main__':
    sample_instructions = ["A", "B", "C"]
    repetition_count = 3
    result = repeat_instructions(sample_instructions, repetition_count)
    print(result)