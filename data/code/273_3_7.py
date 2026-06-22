instructions = {
    "1": "print('First')",
    "2": "print('Second')",
    "3": "print('Third')"
}

if __name__ == '__main__':
    reversed_instructions = [instructions[key] for key in sorted(instructions.keys(), reverse=True)]
    for instruction in reversed_instructions:
        exec(instruction)