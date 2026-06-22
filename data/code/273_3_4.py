def repeat_instructions(instructions, n):
    if not isinstance(instructions, list) or not all(isinstance(instruction, str) for instruction in instructions):
        raise ValueError("Instructions must be a list of strings")
    if not isinstance(n, int) or n < 0:
        raise ValueError("Repeat count must be a non-negative integer")

    reversed_instructions = instructions[::-1]
    result = [eval(instruction) for _ in range(n) for instruction in reversed_instructions]

    return result

if __name__ == '__main__':
    sample_instructions = ["print('Hello')", "print('World')"]
    repeat_count = 3
    try:
        result = repeat_instructions(sample_instructions, repeat_count)
        print(result)
    except ValueError as e:
        print(e)