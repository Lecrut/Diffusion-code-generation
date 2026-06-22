def reverse_repeat(instructions):
    return [instructions[i] for i in range(len(instructions)-1, -1, -1)] * 5

if __name__ == '__main__':
    sample_instructions = ['a', 'b', 'c']
    print(reverse_repeat(sample_instructions))