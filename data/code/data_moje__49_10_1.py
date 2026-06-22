def print_star_square(side_length=5):
    pattern = []
    for _ in range(side_length):
        pattern.append('*' * side_length)
    result = '\n'.join(pattern)
    print(result)
    return result

if __name__ == '__main__':
    print_star_square(5)