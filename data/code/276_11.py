def repeat_instructions(instructions, count):
    return instructions * count
if __name__ == '__main__':
    sample_instructions = ["step 1", "step 2", "step 3"]
    repetition_count = 3
    result = repeat_instructions(sample_instructions, repetition_count)
    print(result)