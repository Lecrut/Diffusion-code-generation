class Repeater:
    def __init__(self, instructions):
        self.instructions = instructions

    def reverse_and_execute(self):
        reversed_instructions = self.instructions[::-1]
        for instruction in reversed_instructions:
            exec(instruction)

if __name__ == '__main__':
    repeater_instance = Repeater(["print('Hello')", "print('World')"])
    repeater_instance.reverse_and_execute()