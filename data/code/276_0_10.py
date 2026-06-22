class InstructionRepeater:
    def __init__(self, instructions):
        self.instructions = instructions

    def repeat(self, n):
        return self.instructions * n

if __name__ == '__main__':
    repeater = InstructionRepeater([1, 2, 3])
    print(repeater.repeat(3))