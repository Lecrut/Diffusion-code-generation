s1 = "Hello"
s2 = "World"
result = lambda x: f"{x}" if not isinstance(x, str) else "".join([str(s1), s2])
if __name__ == '__main__':
    print(result(""))