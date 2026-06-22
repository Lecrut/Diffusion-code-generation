def repeat_instructions():
    instructions = ["print('Hello')", "print('World')"]
    for instruction in reversed(instructions * 5):
        exec(instruction)

if __name__ == '__main__':
    repeat_instructions()