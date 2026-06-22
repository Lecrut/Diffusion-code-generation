def execute_instructions(filename):
    try:
        with open(filename, 'r') as file:
            instructions = file.readlines()
        
        for instruction in instructions:
            parts = instruction.strip().split()
            if len(parts) < 2:
                print(f"Invalid instruction: {instruction}")
                continue
            
            command = parts[0]
            args = parts[1:]
            
            if command == 'print':
                try:
                    value = eval(' '.join(args))
                    print(value)
                except Exception as e:
                    print(f"Error executing print command with arguments {args}: {e}")
            elif command == 'add':
                try:
                    result = sum(map(int, args))
                    print(result)
                except ValueError:
                    print(f"Invalid integer values for add command: {args}")
            else:
                print(f"Unknown command: {command}")

    except FileNotFoundError:
        print(f"File not found: {filename}")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")

if __name__ == '__main__':
    execute_instructions('instructions.txt')