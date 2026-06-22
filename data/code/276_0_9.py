def repeat_instructions(instructions, n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("N must be a non-negative integer")
    repeated = [item for sublist in [instructions] * n for item in sublist]
    return repeated

if __name__ == '__main__':
    instructions = ["print('Hello')", "print('World')"]
    n = 3
    result = repeat_instructions(instructions, n)
    print(result)