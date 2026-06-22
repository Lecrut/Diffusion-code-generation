def repeat_instructions(instructions, N):
    repeated = []
    for _ in range(N):
        repeated.extend(instructions)
    return repeated

if __name__ == '__main__':
    sample_instructions = ['print("Hello")', 'print("World")']
    num_repetitions = 3
    result = repeat_instructions(sample_instructions, num_repetitions)
    print(result)