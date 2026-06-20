# Constants
TRUE = 1
FALSE = 0

def compare_integers(a, b):
    return int(a == b)

if __name__ == '__main__':
    print(compare_integers(5, 5))  # True (1)
    print(compare_integers(3, 4))  # False (0)