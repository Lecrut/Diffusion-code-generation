def print_alphabet_pyramid(height):
    alphabet = [chr(code) for code in range(ord('A'), ord('Z') + 1)]
    lines = [' '.join(alphabet[i - height:i]) for i in range(height)]
    max_width = len(lines[-1])
    for line in lines:
        print(line.center(max_width))

if __name__ == '__main__':
    sample_height = 5
    print_alphabet_pyramid(sample_height)