import re

def rle_encode(text):
    if not text:
        return ''
    encoded = ''
    count = 1
    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            if count > 1:
                encoded += str(count) + text[i - 1]
            else:
                encoded += text[i - 1]
            count = 1
    if count > 1:
        encoded += str(count) + text[-1]
    else:
        encoded += text[-1]
    return encoded

def rle_decode(text):
    if not text:
        return ''
    decoded = ''
    i = 0
    while i < len(text):
        if text[i].isdigit():
            count = int(text[i])
            i += 1
            decoded += text[i] * count
        else:
            decoded += text[i]
        i += 1
    return decoded

if __name__ == '__main__':
    sample = "AAABBBCCCDDDEEEFF"
    encoded = rle_encode(sample)
    print(encoded)
    decoded = rle_decode(encoded)
    print(decoded)