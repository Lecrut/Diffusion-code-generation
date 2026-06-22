class InstructionRepeater:
    def __init__(self, instructions):
        self.instructions = instructions

    def repeat(self, n):
        return [self.instructions for _ in range(n)]

if __name__ == '__main__':
    repeater = InstructionRepeater(['print("Hello")', 'print("World")'])
    repeated_instructions = repeater.repeat(3)
    print(repeated_instructions)