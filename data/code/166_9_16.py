FAVORITE_COLORS = {'red', 'blue', 'green', 'yellow', 'purple'}

def check_color(color):
    return color in FAVORITE_COLORS
if __name__ == '__main__':
    print(check_color('red'))
    print(check_color('orange'))