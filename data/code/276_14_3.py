def instruction_repeater(instructions, repetition_factor):
    for instruction in instructions:
        for _ in range(repetition_factor):
            yield instruction
if __name__ == '__main__':
    sample_instructions = ["move", "jump", "push", "pop"]
    repetition = 3
    repeater = instruction_repeater(sample_instructions, repetition)
    result_list = list(repeater)
    print(result_list)