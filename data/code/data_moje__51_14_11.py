def generate_number_pyramid(height=5):
    result = []
    for i in range(1, height + 1):
        line = ' '.join(str(i) for _ in range(i))
        result.append(line)
    return result

if __name__ == '__main__':
    print(generate_number_pyramid(5))