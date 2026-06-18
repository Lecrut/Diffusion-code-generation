result = (lambda x: lambda y: True if (x > 10) and (y < 50) else False)(20)(30); print(result, result)

if __name__ == '__main__':
    result = ((lambda x: lambda y: bool(x > 10 and y < 50))(70)(49))