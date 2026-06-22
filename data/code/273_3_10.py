def repeat_instructions_reverse():
    instructions = ["print('Hello')", "print('World')"]
    reversed_instructions = instructions[::-1]
    for instruction in reversed_instructions:
        exec(instruction)

if __name__ == '__main__':
    repeat_instructions_reverse()