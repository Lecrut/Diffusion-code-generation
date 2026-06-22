class InstructionExecutor:
    @staticmethod
    def execute_instruction(instruction, count):
        for _ in range(count):
            try:
                exec(instruction)
                break
            except Exception as e:
                print(f"Error executing {instruction}: {e}")

    @staticmethod
    def execute_instructions(instructions):
        executor = InstructionExecutor()
        for instruction, count in instructions.items():
            executor.execute_instruction(instruction, count)

if __name__ == '__main__':
    sample_instructions = {
        'print("Hello")': 3,
        'print("World")': 2
    }
    InstructionExecutor.execute_instructions(sample_instructions)