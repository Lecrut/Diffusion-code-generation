SIDE_LENGTH = 7

def get_square_area(length):
    if length <= 0:
        return 0
    return length * length

if __name__ == '__main__':
    print(get_square_area(SIDE_LENGTH))