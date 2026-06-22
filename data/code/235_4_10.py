H = 4
W = 6

def print_hollow_rectangle(height, width):
    for i in range(height):
        if i == 0 or i == height - 1:
            print('*' * width)
        else:
            print('*' + ' ' * (width - 2) + '*')

if __name__ == '__main__':
    print_hollow_rectangle(H, W)