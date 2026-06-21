if __name__ == '__main__':
    x = 13
    y = 47
    result = (lambda x, y: x > 10 and y < 50)(x, y)
    print(result)