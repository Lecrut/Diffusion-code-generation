result = (lambda x: lambda y: True if x > 10 and y < 50 else False)(x)
if __name__ == '__main__':
    result = (lambda x, y: True if x > 10 and y < 50 else False)(20, 30)