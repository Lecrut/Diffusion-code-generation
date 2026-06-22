def generate_hollow_pyramid(num_rows=5):
    result = []
    for i in range(1, num_rows + 1):
        if i == 1:
            line = ' ' * (num_rows - 1) + str(i)
        elif i == num_rows:
            line = ''.join(str((i - j) % 10 if j == 0 or j == i - 1 else ' ')[j] for j in range(i * 2 - 1))
            line = ' ' * (num_rows - i) + line
        else:
            left = str((i) % 10)
            right = str((i) % 10)
            middle = ' ' * (i * 2 - 3)
            line = ' ' * (num_rows - i) + left + middle + right
        result.append(line)
    return '\n'.join(result)

if __name__ == '__main__':
    print(generate_hollow_pyramid(5))