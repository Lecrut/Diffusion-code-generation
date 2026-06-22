def repeat_instructions(instructions, N):
    repeated = []
    for _ in range(N):
        repeated.extend(instructions)
    return repeated

if __name__ == '__main__':
    instructions = ['print("Hello")', 'print("World")']
    N = 3
    result = repeat_instructions(instructions, N)
    print(result)