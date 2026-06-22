def validate_instructions(instructions):
    if not isinstance(instructions, list) or not all(isinstance(instruction, str) for instruction in instructions):
        raise ValueError("Instructions must be a list of strings")

def validate_count(count):
    if not isinstance(count, int) or count < 1:
        raise ValueError("Count must be a positive integer")

def repeat_instructions(instructions, count):
    validate_instructions(instructions)
    validate_count(count)
    return [instruction for instruction in instructions for _ in range(count)]

if __name__ == '__main__':
    sample_instructions = ["step 1", "step 2", "step 3"]
    repetition_count = 3
    repeated_list = repeat_instructions(sample_instructions, repetition_count)
    print(repeated_list)