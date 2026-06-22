def generate_mirrored_triangle(n):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < 1:
        return []
    result = []
    for i in range(1, n + 1):
        prefix = alphabet[:i]
        mirror = prefix[:-1][::-1]
        result.append(prefix + mirror)
    return result

if __name__ == '__main__':
    rows = 5
    print(generate_mirrored_triangle(rows))