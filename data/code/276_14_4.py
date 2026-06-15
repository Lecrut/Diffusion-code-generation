def instruction_repeater(instructions, repetition_factor):
    for instruction in instructions:
        for _ in range(repetition_factor):
            yield instruction
if __name__ == '__main__':
    sample_instructions = ["A", "B", "C"]
    repetition = 3
    repeater = instruction_repeater(sample_instructions, repetition)
    result_list = []
    for item in repeater:
        result_list.append(item)
    print(result_list)