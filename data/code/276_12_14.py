def execute_instructions(file_path):
    try:
        with open(file_path, 'r') as file:
            instructions = file.readlines()
        
        for instruction in instructions:
            try:
                exec(instruction.strip())
                print(f"Instruction executed successfully: {instruction.strip()}")
            except Exception as e:
                print(f"Error executing instruction: {instruction.strip()} - Error: {e}")

    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    execute_instructions('instructions.txt')