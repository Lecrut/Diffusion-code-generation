def execute_instructions(file_path):
    try:
        with open(file_path, 'r') as file:
            instructions = file.readlines()
        
        for instruction in instructions:
            try:
                exec(instruction)
                print(f"Instruction executed successfully: {instruction.strip()}")
            except Exception as e:
                print(f"Error executing instruction: {instruction.strip()} - {e}")
    except FileNotFoundError:
        print(f"File not found: {file_path}")

if __name__ == '__main__':
    execute_instructions('instructions.txt')