def repeat_instructions(instructions, count):
    if not instructions or not isinstance(count, int) or count < 0:
        return []
    return [inst for inst in instructions for _ in range(count)]

if __name__ == '__main__':
    sample_instructions = ["step 1", "step 2", "step 3"]
    repetition_count = 3
    repeated_list = repeat_instructions(sample_instructions, repetition_count)
    print(repeated_list)