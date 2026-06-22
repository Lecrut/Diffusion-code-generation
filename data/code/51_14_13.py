def generate_number_pyramid(height):
    pyramid = []
    current_number = 1
    for row in range(1, height + 1):
        spaces = ' ' * (height - row)
        numbers = [str(current_number) for _ in range(row)]
        current_number += row
        line = spaces + ' '.join(numbers)
        pyramid.append(line)
    return pyramid

if __name__ == '__main__':
    sample_height = 5
    result = generate_number_pyramid(sample_height)
    for line in result:
        print(line)