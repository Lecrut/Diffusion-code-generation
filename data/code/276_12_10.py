import sys

INSTRUCTION_FILE = "instructions.txt"
COMMAND_PRINT = "print"
COMMAND_ADD = "add"

def execute_instruction(instruction):
    parts = instruction.strip().split()
    if not parts:
        return None
    command = parts[0]
    args = parts[1:]
    if command == COMMAND_PRINT:
        print(*args)
    elif command == COMMAND_ADD:
        result = sum(map(int, args))
        print(result)
    else:
        raise ValueError(f"Unknown command: {command}")

def execute_instructions(file_path):
    try:
        with open(file_path, 'r') as file:
            instructions = file.readlines()
        for instruction in instructions:
            execute_instruction(instruction)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except ValueError as e:
        print(f"Error executing instruction: {e}")

if __name__ == '__main__':
    sample_file_path = INSTRUCTION_FILE
    execute_instructions(sample_file_path)