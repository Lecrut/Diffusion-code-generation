def repeat_instructions(instructions, n):
    return [ins for ins in instructions] * n

if __name__ == '__main__':
    sample_instructions = ['print("Hello")', 'print("World")']
    repetitions = 3
    repeated_instructions = repeat_instructions(sample_instructions, repetitions)
    print(repeated_instructions)