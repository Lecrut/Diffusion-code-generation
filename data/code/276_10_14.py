def read_instructions(filepath):
    try:
        with open(filepath, 'r') as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        return []

def repeat_instructions(instructions, count):
    for instruction in instructions:
        for _ in range(count):
            print(instruction)

if __name__ == '__main__':
    sample_content = [
        "Instruction one",
        "Instruction two",
        "Instruction three"
    ]
    with open('instructions.txt', 'w') as f:
        for line in sample_content:
            f.write(line + '\n')
    
    instructions = read_instructions('instructions.txt')
    repeat_instructions(instructions, 3)