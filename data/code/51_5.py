def generate_hollow_pyramid(rows):
    lines = []
    for i in range(rows):
        spaces = ' ' * (rows - i - 1)
        if i == 0:
            digits = '1'
        elif i == rows - 1:
            digits = ' '.join(str(j + 1) for j in range(i + 1))
        else:
            if i < 9:
                first = str(i + 1)
                last = str(i + 1)
            else:
                first = str(i + 1)[-1]
                last = str(i + 1)[-1]
            
            hollow_part = ' '
            for _ in range(i - 1):
                hollow_part += '  '
            
            digits = f"{first}{hollow_part}{last}"
        
        full_line = f"{spaces}{digits}"
        lines.append(full_line)
    return '\n'.join(lines)

if __name__ == '__main__':
    print(generate_hollow_pyramid(5))