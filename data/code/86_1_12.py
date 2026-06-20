comparison_map = {True: 'True', False: 'False'}

def compare_booleans(a, b):
    return comparison_map[a == b]

if __name__ == '__main__':
    print(compare_booleans(True, True))
    print(compare_booleans(False, False))
    print(compare_booleans(True, False))
    print(compare_booleans(False, True))