def repeat_instructions(instructions, N):
    return [instructions for _ in range(N)]

if __name__ == '__main__':
    sample_instructions = ['print("Hello")', 'print("World")']
    repeated_instructions = repeat_instructions(sample_instructions, 3)
    print(repeated_instructions)