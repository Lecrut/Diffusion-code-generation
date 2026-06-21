MAX_VALUE = float('-inf')

def max_element(*args):
    return max(args, default=MAX_VALUE)

if __name__ == '__main__':
    print(max_element(10, 5, 20, 8, 15))