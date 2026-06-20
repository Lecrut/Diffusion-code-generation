MAX_AGE = 18

def get_max(a, b):
    return a if a > b else b

if __name__ == '__main__':
    print(get_max(5, 3))