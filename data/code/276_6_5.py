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
                        if args:
                            print(f"Executing instruction {line_number + 1}: {command} with argument '{args[0]}' (Run {i + 1}/10)")
                        else:
                            print(f"Executing instruction {line_number + 1}: {command} (Run {i + 1}/10)")
                    else:
                        print(f"Executing instruction {line_number + 1}: {command} (Run {i + 1}/10)")
                except Exception as e:
                    print(f"Error executing line {line_number + 1}, iteration {i + 1}: {e}", file=sys.stderr)
        except Exception as e:
            print(f"Error parsing instruction on line {line_number + 1}: '{instruction}'. Error: {e}", file=sys.stderr)
if __name__ == '__main__':
    sample_filename = "instructions.txt"
    try:
        with open(sample_filename, 'w') as f:
            f.write("# This is a sample instruction file\n")
            f.write("execute value_a\n")
            f.write("print result\n")
            f.write("set flag true\n")
            f.write("\n")
        execute_instructions(sample_filename)
    except IOError as e:
        print(f"Fatal error setting up sample file: {e}", file=sys.stderr)