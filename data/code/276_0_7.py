def repeat_instructions(instructions, n):
    return instructions * n

if __name__ == '__main__':
    sample_instructions = ['print("Hello")', 'print("World")']
    repeated_instructions = repeat_instructions(sample_instructions, 3)
    for instruction in repeated_instructions:
        exec(instruction)