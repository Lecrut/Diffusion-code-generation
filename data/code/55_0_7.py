def print_right_aligned_alphabet_triangle(max_letter):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if max_letter not in alphabet:
        raise ValueError("max_letter must be an uppercase letter A-Z")
    
    target_index = alphabet.index(max_letter)
    max_width = (target_index + 1) * 2
    
    for i in range(target_index + 1):
        row_letters = alphabet[i]
        row_string = " ".join([alphabet[j] for j in range(i + 1)])
        print(row_string.rjust(max_width))

if __name__ == "__main__":
    sample_max = "D"
    print_right_aligned_alphabet_triangle(sample_max)