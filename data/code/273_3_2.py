def repeat_instructions():
    instructions = ["print('Hello')", "print('World')"]
    reversed_instructions = [instructions[i] for i in range(len(instructions)-1, -1, -1)]
    for instruction in reversed_instructions:
        exec(instruction)

if __name__ == '__main__':
    repeat_instructions()