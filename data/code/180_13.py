lambda s1, s2: s2.lower() in s1.lower()
if __name__ == '__main__':
    print(lambda s1, s2: s2.lower() in s1.lower()("HelloWorld", "world"))
    print(lambda s1, s2: s2.lower() in s1.lower()("Programming", "gram"))
    print(lambda s1, s2: s2.lower() in s1.lower()("Apple", "banana"))