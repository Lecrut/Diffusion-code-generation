instructions = ["print('Task')", "print('Completed')"]

def reverse_and_repeat(instructions):
    reversed_instructions = instructions[::-1]
    for instruction in reversed_instructions:
        exec(instruction)

if __name__ == '__main__':
    sample_instructions = instructions
    reverse_and_repeat(sample_instructions)