class Repeater:
    def __init__(self, instructions):
        self.instructions = instructions

    def reverse_and_repeat(self, n):
        reversed_instructions = self.instructions[::-1]
        for _ in range(n):
            for instruction in reversed_instructions:
                exec(instruction)

if __name__ == '__main__':
    repeater = Repeater(["print('First')", "print('Second')", "print('Third')"])
    repeater.reverse_and_repeat(5)