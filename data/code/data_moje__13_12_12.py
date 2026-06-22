def fetch_element(s, n):
    if n >= 0:
        if n < len(s):
            return s[n]
        return None
    if n < 0 and abs(n) <= len(s):
        return s[n]
    return None

if __name__ == '__main__':
    text = "HelloWorld"
    index_positive = 4
    index_negative = -2
    result1 = fetch_element(text, index_positive)
    result2 = fetch_element(text, index_negative)
    print(result1)
    print(result2)