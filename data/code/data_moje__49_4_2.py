def generate_star_square():
    return ['* * * *'] * 4

if __name__ == '__main__':
    result = generate_star_square()
    for line in result:
        print(line)