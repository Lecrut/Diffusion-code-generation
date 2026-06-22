def read_integers(filename):
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
        integers = [int(line.strip()) for line in lines if line.strip().isdigit()]
        return integers
    except IOError as e:
        print(f"Error reading file {filename}: {e}")
        return []

def repeat_integers(integers, S):
    return [num for num in integers for _ in range(S)]

if __name__ == '__main__':
    sample_filename = 'sample.txt'
    sample_S = 3
    integers = read_integers(sample_filename)
    repeated_integers = repeat_integers(integers, sample_S)
    print(repeated_integers)