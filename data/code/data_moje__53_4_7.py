import itertools

def generate_reverse_triangle(height):
    for i in range(height, 0, -1):
        numbers = []
        for j in range(1, i + 1):
            numbers.append(str(j))
        yield ' '.join(reversed(numbers))

if __name__ == '__main__':
    for row in generate_reverse_triangle(3):
        print(row)