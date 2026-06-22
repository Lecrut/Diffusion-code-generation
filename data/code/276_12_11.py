def execute_instructions(file_path):
    try:
        with open(file_path, 'r') as file:
            instructions = file.readlines()
        results = []
        for instruction in instructions:
            parts = instruction.strip().split()
            if not parts:
                continue
            command = parts[0]
            args = parts[1:]
            if command == 'print':
                result = ' '.join(args)
                print(result)
                results.append(result)
            elif command == 'add':
                numbers = list(map(int, args))
                result = sum(numbers)
                print(f"Sum: {result}")
                results.append(result)
            else:
                raise ValueError(f"Unknown command: {command}")
        return results
    except FileNotFoundError:
        print("File not found.")
        return None

if __name__ == '__main__':
    sample_instructions_path = 'sample_instructions.txt'
    execute_instructions(sample_instructions_path)