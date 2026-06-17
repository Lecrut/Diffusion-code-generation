def repeat_instructions(instructions, count):
    return instructions * count
if __name__ == '__main__':
    sample_instructions = ["Step 1", "Step 2", "Step 3"]
    repetition_count = 3
    result = repeat_instructions(sample_instructions, repetition_count)
    print(result)