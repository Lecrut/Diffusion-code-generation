def generate_number_pyramid(size=6):
    return [
        ''.join([str((i + 1) % 10) for _ in range(i + 1)])
        for i in range(size)
    ]

if __name__ == '__main__':
    print(generate_number_pyramid())