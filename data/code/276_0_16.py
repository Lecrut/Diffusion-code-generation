def repeat_instructions(instructions, n):
    return instructions * n

if __name__ == '__main__':
    sample_instructions = ['print("Hello")', 'print("World")']
    num_repetitions = 3
    repeated_instructions = repeat_instructions(sample_instructions, num_repetitions)
    print(repeated_instructions)