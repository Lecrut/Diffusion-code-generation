result = (lambda x: lambda y: bool((1 if x > 10 else 0) and not (y >= 50)))(x, y); print(result)

if __name__ == '__main__':
    pass
