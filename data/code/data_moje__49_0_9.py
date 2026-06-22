def draw_star_square(side_length):
    result = ""
    for row in range(side_length):
        line = ""
        for col in range(side_length):
            line += "*"
        result += line + "\n"
    return result

if __name__ == '__main__':
    side_length = 5
    print(draw_star_square(side_length), end="")