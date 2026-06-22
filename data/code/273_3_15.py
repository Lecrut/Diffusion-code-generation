class InstructionRepeater:
    INSTRUCTIONS = ["print('First')", "print('Second')", "print('Third')"]

    @staticmethod
    def reverse_and_execute():
        reversed_instructions = InstructionRepeater.INSTRUCTIONS[::-1]
        for instruction in reversed_instructions:
            exec(instruction)

if __name__ == '__main__':
    InstructionRepeater.reverse_and_execute()