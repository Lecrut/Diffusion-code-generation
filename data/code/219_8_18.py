MAX_NUMBER = 100

def max_squared():
    return max(x**2 for x in range(1, MAX_NUMBER + 1))

if __name__ == '__main__':
    print(max_squared())