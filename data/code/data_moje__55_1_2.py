def print_centered_alphabet_triangle(height: int) -> None:
    if height <= 0:
        return
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if height > len(alphabet):
        height = len(alphabet)
    max_width = (height - 1) * 2 + 1
    for i in range(1, height + 1):
        start_index = len(alphabet) // 2 - i // 2 if height % 2 != 0 else len(alphabet) // 2 - (i - 1) // 2
        if height % 2 == 0 and i % 2 == 1:
             start_index = len(alphabet) // 2 - (i - 1) // 2
        elif height % 2 == 0 and i % 2 == 0:
             start_index = len(alphabet) // 2 - (i - 1) // 2
        else:
             start_index = (len(alphabet) - i) // 2
        
        letters = []
        current_idx = start_index
        while len(letters) < i:
            letters.append(alphabet[current_idx])
            current_idx += 1
        letters = letters[0]
        for k in range(1, i):
            letters += alphabet[start_index + k]
        
        left_half = []
        right_half = []
        if height % 2 != 0:
            idx = (len(alphabet) - i) // 2
        else:
            idx = (len(alphabet) - i) // 2
            if i % 2 != 0 and height % 2 == 0:
                idx = (len(alphabet) - i) // 2
        
        if i == 1:
             char = alphabet[len(alphabet) // 2 - (height - 1) // 2]
             line = char.center(max_width)
             print(line)
             continue

        chars = []
        current = 0
        if height % 2 != 0:
            current = (len(alphabet) - i) // 2
        else:
            current = (len(alphabet) - i) // 2
        
        for _ in range(i):
            chars.append(alphabet[current])
            current += 1
        
        left = "".join(chars)
        right = "".join(chars[-2::-1])
        line = left + right
        
        padding = (max_width - len(line)) // 2
        print(" " * padding + line)

if __name__ == '__main__':
    print_centered_alphabet_triangle(5)