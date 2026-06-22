def render_diamond_alphabet(height):
    if height <= 0:
        return ''
    lines = []
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in range(height):
        letters_needed = i + 1
        spaces = height - i - 1
        prefix = ' ' * spaces
        suffix = ' ' * spaces
        if letters_needed <= len(alphabet):
            first_half = alphabet[:letters_needed]
            second_half = alphabet[1:letters_needed][::-1]
            line = prefix + first_half + second_half + suffix
        else:
            full_set = alphabet + alphabet[-1:-letters_needed + len(alphabet):-1]
            adjusted = full_set[:letters_needed * 2 - 1]
            line = prefix + adjusted + suffix
        lines.append(line)
    for i in range(height - 2, -1, -1):
        letters_needed = i + 1
        spaces = height - i - 1
        prefix = ' ' * spaces
        suffix = ' ' * spaces
        if letters_needed <= len(alphabet):
            first_half = alphabet[:letters_needed]
            second_half = alphabet[1:letters_needed][::-1]
            line = prefix + first_half + second_half + suffix
        else:
            full_set = alphabet + alphabet[-1:-letters_needed + len(alphabet):-1]
            adjusted = full_set[:letters_needed * 2 - 1]
            line = prefix + adjusted + suffix
        lines.append(line)
    return '\n'.join(lines)
if __name__ == '__main__':
    result = render_diamond_alphabet(5)
    print(result)