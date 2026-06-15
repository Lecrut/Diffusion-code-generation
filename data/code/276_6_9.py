import sys
def execute_instructions(filename):
    try:
        with open(filename, 'r') as f:
            instructions = f.readlines()
    except IOError as e:
        print(f"Error reading file {filename}: {e}", file=sys.stderr)
        return
    for line_number, instruction in enumerate(instructions):
        instruction = instruction.strip()
        if not instruction or instruction.startswith('#'):
            continue
        try:
            instruction_parts = instruction.split()
            if not instruction_parts:
                continue
            command = instruction_parts[0]
            args = instruction_parts[1:]
            for i in range(10):
                try:
                    if command == "execute":
                        print(f"Executing instruction {line_number + 1}: {instruction} (Run {i + 1}/10)")
                    else:
                        print(f"Warning: Unknown command '{command}' in line {line_number + 1}. Skipping execution.", file=sys.stderr)
                except Exception as e:
                    print(f"Error executing instruction on line {line_number + 1} during run {i + 1}: {e}", file=sys.stderr)
        except Exception as e:
            print(f"Error parsing or processing line {line_number + 1}: '{instruction}'. Error: {e}", file=sys.stderr)
if __name__ == '__main__':
    sample_filename = "instructions.txt"
    try:
        with open(sample_filename, 'w') as f:
            f.write("# This is a sample instruction file\n")
            f.write("execute step_a\n")
            f.write("execute step_b\n")
            f.write("skip_this\n")
            f.write("\n")
        execute_instructions(sample_filename)
    except IOError as e:
        print(f"Fatal error setting up sample file: {e}", file=sys.stderr)