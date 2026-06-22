def repeat_instructions(instructions, n):
    if not isinstance(instructions, list) or not all(isinstance(i, str) for i in instructions):
        raise ValueError("Instructions must be a list of strings.")
    if not isinstance(n, int) or n < 0:
        raise ValueError("N must be a non-negative integer.")

    repeated_instructions = [i * n for i in instructions]
    return repeated_instructions

if __name__ == '__main__':
    sample_instructions = ["print('Hello')", "print('World')"]
    times_to_repeat = 3
    try:
        result = repeat_instructions(sample_instructions, times_to_repeat)
        print(result)
    except ValueError as e:
        print(e)