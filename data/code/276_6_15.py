def repeat_integers(filename, S):
    try:
        with open(filename, 'r') as f:
            numbers = list(map(int, f.read().split()))
    except IOError as e:
        print(f"Error reading file {filename}: {e}")
        return []
    repeated_numbers = [number for number in numbers for _ in range(S)]
    return repeated_numbers

if __name__ == '__main__':
    result = repeat_integers('sample.txt', 3)
    print(result)