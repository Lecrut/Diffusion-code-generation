def repeat_instructions(instructions, N):
    if not isinstance(instructions, list) or not all(isinstance(i, str) for i in instructions):
        raise ValueError("Instructions must be a list of strings.")
    if not isinstance(N, int) or N < 1:
        raise ValueError("N must be a positive integer.")

    repeated_instructions = [instr for instr in instructions for _ in range(N)]
    return repeated_instructions

if __name__ == '__main__':
    sample_instructions = ["print('Hello')", "print('World')"]
    N = 3
    result = repeat_instructions(sample_instructions, N)
    print(result)