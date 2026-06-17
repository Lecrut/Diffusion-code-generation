import os
def read_instructions(filepath):
    try:
        with open(filepath, 'r') as f:
            return f.readlines()
    except FileNotFoundError:
        return []
def main():
    instructions_file = "instructions.txt"
    sample_content = [
        "Instruction one",
        "Instruction two",
        "Instruction three"
    ]
    with open(instructions_file, 'w') as f:
        for line in sample_content:
            f.write(line + '\n')
    instructions = read_instructions(instructions_file)
    if not instructions:
        return
    for instruction in instructions:
        print(instruction)
        print(instruction)
        print(instruction)
if __name__ == '__main__':
    main()