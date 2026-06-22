def generate_centered_alphabet_triangle(n):
    if n < 1:
        return []
    
    result = []
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    for i in range(1, n + 1):
        current_row_chars = [alphabet[j] for j in range(i)]
        current_row_str = ''.join(current_row_chars)
        padding = ' ' * (n - i)
        line = padding + current_row_str + padding
        result.append(line)
    
    return result

if __name__ == '__main__':
    sample_size = 5
    output = generate_centered_alphabet_triangle(sample_size)
    print(output)