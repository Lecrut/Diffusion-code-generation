import sys
def execute_instructions(filepath):
    try:
        with open(filepath, 'r') as f:
            instructions = f.readlines()
    except IOError as e:
        print(f"Error reading file {filepath}: {e}", file=sys.stderr)
        return
    for line_number, instruction in enumerate(instructions):
        instruction = instruction.strip()
        if not instruction or instruction.startswith('#'):
            continue
        try:
            for i in range(10):
                print(f"Executing instruction '{instruction}' (Run {i + 1}/10)")
        except Exception as e:
            print(f"Error executing instruction on line {line_number + 1}: {e}", file=sys.stderr)
if __name__ == '__main__':
    sample_filename = "instructions.txt"
    try:
        with open(sample_filename, 'w') as f:
            f.write("Add 1\n")
            f.write("Multiply by 2\n")
            f.write("Subtract 5\n")
            f.write("# This is a comment\n")
            f.write("Divide by 3\n")
        execute_instructions(sample_filename)
    except IOError as e:
        print(f"Fatal error setting up sample file: {e}", file=sys.stderr)