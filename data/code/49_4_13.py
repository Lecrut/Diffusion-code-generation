def create_star_square():
    return ['* * * *', '* * * *', '* * * *', '* * * *']

if __name__ == '__main__':
    result = create_star_square()
    for line in result:
        print(line)