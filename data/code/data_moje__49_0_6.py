def print_square(n):
    result = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append('*')
        result.append(''.join(row))
    return '\n'.join(result)

if __name__ == '__main__':
    print(print_square(5))