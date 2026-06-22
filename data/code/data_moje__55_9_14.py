import string

def generate_mirrored_triangle(n):
    alphabet = string.ascii_uppercase
    if n <= 0:
        return []
    result = []
    for i in range(1, n + 1):
        prefix = alphabet[:i]
        mirror = prefix[:-1][::-1]
        result.append(prefix + mirror)
    return result

if __name__ == '__main__':
    sample_size = 5
    pattern = generate_mirrored_triangle(sample_size)
    for line in pattern:
        print(line)