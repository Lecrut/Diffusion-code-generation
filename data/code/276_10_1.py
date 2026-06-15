def main():
    instructions_file = "instructions.txt"
    repeated_count = 3
    try:
        with open(instructions_file, 'r') as f:
            instructions = f.readlines()
    except FileNotFoundError:
        print(f"Error: The file {instructions_file} was not found.")
        return
    for instruction in instructions:
        print(instruction.strip())
        for _ in range(repeated_count - 1):
            print(instruction.strip())
if __name__ == '__main__':
    main()