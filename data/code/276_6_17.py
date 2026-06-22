def repeat_integers(filename, S):
    try:
        with open(filename, 'r') as f:
            numbers = [int(line.strip()) for line in f if line.strip().isdigit()]
    except IOError as e:
        print(f"Error reading file {filename}: {e}", file=sys.stderr)
        return []
    
    repeated_numbers = [number for number in numbers for _ in range(S)]
    return repeated_numbers

if __name__ == '__main__':
    sample_filename = 'sample.txt'
    S = 3
    result = repeat_integers(sample_filename, S)
    print(result)