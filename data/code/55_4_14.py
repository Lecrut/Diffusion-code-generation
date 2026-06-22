def generate_pyramid(n):
    return '\n'.join(
        ' '.join(chr(ord('A') + j) for j in range(i)) 
        for i in range(1, n + 1)
    )

if __name__ == '__main__':
    print(generate_pyramid(5))