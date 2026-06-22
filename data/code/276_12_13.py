class InstructionExecutor:
    def execute(self, file_path):
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
                    print(result)
                else:
                    raise ValueError(f"Unknown command: {command}")
        except FileNotFoundError:
            print("File not found. Please provide a valid file path.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == '__main__':
    executor = InstructionExecutor()
    sample_file_path = "sample_instructions.txt"
    result = executor.execute(sample_file_path)