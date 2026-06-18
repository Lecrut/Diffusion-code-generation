def main():
    s1 = "Hello"
    s2 = "World"
    result = f"{s1}{s2}" if isinstance(s1, str) and isinstance(s2, str) else ""
    print(result)
if __name__ == '__main__':
    main()