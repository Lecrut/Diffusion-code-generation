def generate_pyramid(height):
    result = []
    for i in range(1, height + 1):
        nums = [str(j) for j in range(1, i + 1)]
        row = ' '.join(nums)
        padding = ' ' * (height - i)
        line = padding + row + padding
        result.append(line.strip())
    return result

if __name__ == '__main__':
    height = 5
    pyramid = generate_pyramid(height)
    print(pyramid)