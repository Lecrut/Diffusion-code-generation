result = (lambda x: lambda y: True if (x > 10) and (y < 50) else False)(25)(30)
if __name__ == '__main__':
    result = (lambda x, y: bool(x > 10 and y < 50))(25)(30)