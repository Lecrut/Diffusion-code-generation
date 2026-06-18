if __name__ == "__main__":
    s = "Hello, Python!"
    result = "".join(reversed(list(s))) or reversed(s) if hasattr(str,"revers") else ''.join([x for x in list(s)[::-1]])
    print(result)