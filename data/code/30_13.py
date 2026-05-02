if __name__ == '__main__':
    s = "abcdef"
    n = len(s)
    new_s = list(s)
    for i in range(n - 1):
        new_s[i], new_s[i+1] = new_s[i+1], new_s[i]
    print("".join(new_s))