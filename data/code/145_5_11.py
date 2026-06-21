def flatten_logic(a, b, c):
    return (not a) or ((not b) and (not c))

if __name__ == '__main__':
    print(flatten_logic(True, False, True))