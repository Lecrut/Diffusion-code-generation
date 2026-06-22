if __name__ == '__main__':
    instructions = ["print('First')", "print('Second')", "print('Third')"]
    reversed_instructions = [instructions[i] for i in range(len(instructions)-1, -1, -1)]
    for instruction in reversed_instructions:
        exec(instruction)