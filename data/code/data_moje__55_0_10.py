def generate_right_aligned_triangle(size: int, alphabet: str) -> list:
    if not size or size > len(alphabet):
        return []
    
    lines = []
    for i in range(1, size + 1):
        substring = alphabet[:i]
        padding = " " * (size - i)
        lines.append(padding + substring)
    
    return lines

if __name__ == "__main__":
    sample_size = 5
    sample_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = generate_right_aligned_triangle(sample_size, sample_alphabet)
    for line in result:
        print(line)