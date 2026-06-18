s1 = "Hello"
s2 = "World"
result = lambda s: f"{s[0]}{s[1]}" if len(s) >= 2 else ""
print(result((s1, s2)))
if __name__ == '__main__':
    print("Success")