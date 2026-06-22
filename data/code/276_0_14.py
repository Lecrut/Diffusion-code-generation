class InstructionRepeater:
    def __init__(self, instructions):
        self.instructions = instructions

    def repeat(self, N):
        return [self.instructions[:] for _ in range(N)]

if __name__ == '__main__':
    repeater = InstructionRepeater(['move forward', 'turn right'])
    repeated_instructions = repeater.repeat(3)
    print(repeated_instructions)