def generate_number_pyramid(height):
    result = []
    for i in range(1, height + 1):
        spaces = ' ' * (height - i)
        numbers = ' '.join(str(min(j, 2 * i - 1 - j + 1)) for j in range(1, 2 * i))
        result.append(spaces + numbers)
    return result

if __name__ == '__main__':
    print(generate_number_pyramid(5))