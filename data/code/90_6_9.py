def check_conditions(a, b, c):
    return a | b | c

if __name__ == '__main__':
    print(check_conditions(0b101, 0b010, 0b111))