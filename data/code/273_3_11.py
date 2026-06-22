def reverse_and_repeat(instructions):
    if not instructions:
        return []
    reversed_instructions = instructions[::-1]
    result = [f"{instruction}()" for instruction in reversed_instructions]
    return result

if __name__ == '__main__':
    sample_instructions = ["print('Hello')", "print('World')"]
    repeated_instructions = reverse_and_repeat(sample_instructions)
    for instruction in repeated_instructions:
        exec(instruction)