a = "Hello"
b = "World"
result = lambda x: f"{x[0]}{x[1]}" if isinstance(x, tuple) else ""
if __name__ == '__main__':
    print(result((a, b)))