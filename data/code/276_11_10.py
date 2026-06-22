def repeat_instructions(instructions, times):
    if not isinstance(times, int) or times < 0:
        raise ValueError("Repeat count must be a non-negative integer")
    return [inst for inst in instructions for _ in range(times)]

if __name__ == '__main__':
    sample_instructions = ["Move forward", "Turn right"]
    repeat_count = 3
    repeated_instructions = repeat_instructions(sample_instructions, repeat_count)
    print(repeated_instructions)