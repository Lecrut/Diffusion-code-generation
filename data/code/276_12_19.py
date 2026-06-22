class InstructionExecutor:
    COMMAND_MAP = {'print': lambda args: print(*args), 'add': lambda args: sum(map(int, args))}

    @staticmethod
    def execute_command(command, args):
        if command in InstructionExecutor.COMMAND_MAP:
            return InstructionExecutor.COMMAND_MAP[command](args)
        else:
            raise ValueError(f'Unknown command: {command}')

    def execute_file(self, file_path):
        try:
            with open(file_path, 'r') as file:
                instructions = file.readlines()
            for instruction in instructions:
                parts = instruction.strip().split()
                if not parts:
                    continue
                command = parts[0]
                args = parts[1:]
                result = self.execute_command(command, args)
                print(result)
        except FileNotFoundError:
            print(f'File not found: {file_path}')
        except ValueError as e:
            print(e)
if __name__ == '__main__':
    executor = InstructionExecutor()
    sample_file_path = 'instructions.txt'
    executor.execute_file(sample_file_path)