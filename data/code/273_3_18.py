def repeat_instructions():
    instructions = [
        "print('Step 1')",
        "print('Step 2')",
        "print('Step 3')",
        "print('Step 4')",
        "print('Step 5')"
    ]
    reversed_instructions = instructions[::-1]
    for instruction in reversed_instructions:
        exec(instruction)

if __name__ == '__main__':
    repeat_instructions()