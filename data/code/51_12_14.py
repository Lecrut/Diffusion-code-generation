def generate_number_pyramid(size=6):
    pyramid = [
        ' '.join(
            str(num) if num % 2 == 0 else str((num + 1) // 2)
            for num in range(1, i * 2)
        ).strip()
        for i in range(1, size + 1)
    ]
    return pyramid

if __name__ == '__main__':
    print(generate_number_pyramid(6))