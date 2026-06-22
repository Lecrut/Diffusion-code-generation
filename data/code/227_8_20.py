def print_heart_star():
    pattern = {
        0: "   *   ",
        1: "  ***  ",
        2: " ***** ",
        3: "*******",
        4: " ***** ",
        5: "  ***  ",
        6: "   *   "
    }
    for index in range(7):
        print(pattern[index])

if __name__ == '__main__':
    print_heart_star()