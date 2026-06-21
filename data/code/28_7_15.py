def rle_generator(s):
    if not s:
        return
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            yield s[i - 1], count
            count = 1
    yield s[-1], count

if __name__ == '__main__':
    sample_string = "aaabbccccd"
    encoded_result = list(rle_generator(sample_string))
    print(encoded_result)