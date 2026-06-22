class InstructionExecutor:
    DEFAULT_MAX_RETRIES = 3

    @staticmethod
    def execute_instruction(instruction, count):
        for _ in range(count):
            try:
                exec(instruction)
                break
            except Exception as e:
                print(f"Error executing {instruction}: {e}")
                if _ < InstructionExecutor.DEFAULT_MAX_RETRIES - 1:
                    continue
                raise

    @staticmethod
    def execute_instructions(instructions):
        for instruction, count in instructions.items():
            InstructionExecutor.execute_instruction(instruction, count)

if __name__ == '__main__':
    sample_instructions = {
        'print("Hello")': 3,
        'print("World")': 2
    }
    InstructionExecutor.execute_instructions(sample_instructions)