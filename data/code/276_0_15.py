def repeat_instructions(instructions, n):
    return instructions * n

if __name__ == '__main__':
    sample_instructions = ['print("Hello")', 'print("World")']
    repetitions = 3
    result = repeat_instructions(sample_instructions, repetitions)
    for instruction in result:
        exec(instruction)