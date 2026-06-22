def execute_instructions(file_path):
    try:
        with open(file_path, 'r') as file:
            instructions = file.readlines()
        
        results = []
        for instruction in instructions:
            parts = instruction.strip().split()
            if len(parts) == 2 and parts[0] == "print":
                result = eval(parts[1])
                results.append(result)
            else:
                raise ValueError(f"Invalid instruction: {instruction}")
        
        return results
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"Error executing instructions: {e}")

if __name__ == '__main__':
    sample_file_path = 'instructions.txt'
    results = execute_instructions(sample_file_path)
    for result in results:
        print(result)