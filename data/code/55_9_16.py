def generate_mirrored_alphabet_triangle(height):
    if height <= 0:
        return ""
    
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if height > 26:
        height = 26
        
    lines = []
    for i in range(1, height + 1):
        current_letters = alphabet[:i]
        center_idx = i - 1
        right_side = current_letters[:center_idx]
        left_side = current_letters[:center_idx]
        
        if i == 1:
            left_part = left_side
        else:
            reversed_right = right_side[::-1]
            left_part = reversed_right + current_letters[-1]
            
        line = left_part
        
        lines.append(line)
        
    result = "\n".join(lines)
    return result

if __name__ == '__main__':
    sample_height = 5
    output = generate_mirrored_alphabet_triangle(sample_height)
    print(output)