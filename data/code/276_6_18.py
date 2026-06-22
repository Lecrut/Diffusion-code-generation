def repeat_integers(filename, S):
    try:
        with open(filename, 'r') as f:
            numbers = [int(line.strip()) for line in f if line.strip().isdigit()]
    except (FileNotFoundError, ValueError) as e:
        print(f"Error reading file {filename}: {e}", file=sys.stderr)
        return []

    repeated_numbers = [num for num in numbers for _ in range(S)]
    return repeated_numbers

if __name__ == '__main__':
    result = repeat_integers('input.txt', 3)
    print(result)