def execute_instructions(file_path):
    try:
        with open(file_path, 'r') as file:
            instructions = file.readlines()
        
        for instruction in instructions:
            parts = instruction.strip().split()
            if not parts:
                continue
            
            command = parts[0]
            args = parts[1:]
            
            if command == 'print':
                print(*args)
            elif command == 'add':
                result = sum(map(int, args))
                print(f"Sum: {result}")
            else:
                print(f"Unknown command: {command}")

    except FileNotFoundError:
        print("File not found.")
    except ValueError:
        print("Invalid argument for arithmetic operation.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    execute_instructions('instructions.txt')