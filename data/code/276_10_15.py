def repeat_instructions(instructions, repetitions):
    for instruction in instructions:
        for _ in range(repetitions):
            print(instruction)

if __name__ == '__main__':
    sample_instructions = {
        "step1": "Initialize variables",
        "step2": "Read input data",
        "step3": "Process data"
    }
    repeated_count = 3
    instructions_to_repeat = [sample_instructions[key] for key in sample_instructions]
    repeat_instructions(instructions_to_repeat, repeated_count)