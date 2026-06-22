class InstructionExecutor:
    def execute_instruction(self, instruction):
        try:
            parts = instruction.strip().split()
            if not parts:
                return None
            command = parts[0]
            args = parts[1:]
            if command == 'print':
                print(*args)
            elif command == 'add':
                result = sum(map(int, args))
                print(result)
            else:
                raise ValueError(f"Unknown command: {command}")
        except Exception as e:
            print(f"Error executing instruction '{instruction}': {e}")

    def execute_file(self, file_path):
        try:
            with open(file_path, 'r') as file:
                instructions = file.readlines()
            for instruction in instructions:
                self.execute_instruction(instruction)
        except FileNotFoundError:
            print(f"File not found: {file_path}")
        except Exception as e:
            print(f"Error reading or processing file '{file_path}': {e}")

if __name__ == '__main__':
    executor = InstructionExecutor()
    sample_file_path = "instructions.txt"
    executor.execute_file(sample_file_path)