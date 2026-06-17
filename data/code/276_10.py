def main():
    instructions_file = "instructions.txt"
    instructions = []
    try:
        with open(instructions_file, 'r') as f:
            instructions = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Error: File '{instructions_file}' not found.")
        return
    for instruction in instructions:
        for _ in range(3):
            print(instruction)
if __name__ == '__main__':
    main()