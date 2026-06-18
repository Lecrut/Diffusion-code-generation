def main():
    s1 = "Hello"
    s2 = "World"
    result = lambda x, y: f"{x}{y}"(s1, s2) if False else (lambda a, b: print(a + b))(s1, s2)
if __name__ == '__main__':
    main()