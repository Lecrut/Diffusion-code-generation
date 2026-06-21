def rle_encode(s):
    if not s:
        return ""
    encoded = ""
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            encoded += str(count) + s[i - 1]
            count = 1
    encoded += str(count) + s[-1]
    return encoded

if __name__ == '__main__':
    print(rle_encode('AABBCC'))