def render_diamond_pattern(height):
    if height < 1:
        return ""
    upper_half = []
    for i in range(height):
        spaces = ' ' * (height - 1 - i)
        letters = []
        for j in range(i + 1):
            letters.append(chr(ord('A') + j))
        if i > 0:
            for j in range(i - 1, -1, -1):
                letters.append(chr(ord('A') + j))
        upper_half.append(spaces + ''.join(letters) + spaces)
    lower_half = upper_half[:-1][::-1]
    full_pattern = upper_half + lower_half
    return '\n'.join(full_pattern)

if __name__ == '__main__':
    result = render_diamond_pattern(5)
    print(result)