class RLE:
    def encode(self, s):
        if not s:
            return ""
        result = []
        count = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                result.append(str(count) + s[i - 1])
                count = 1
        result.append(str(count) + s[-1])
        return "".join(result)

    def decode(self, s):
        if not s:
            return ""
        result = []
        i = 0
        while i < len(s):
            num_str = ""
            while i < len(s) and s[i].isdigit():
                num_str += s[i]
                i += 1
            if i < len(s):
                char = s[i]
                count = int(num_str)
                result.append(char * count)
                i += 1
        return "".join(result)

if __name__ == '__main__':
    rle = RLE()
    original = "aaabbbcccaa"
    encoded = rle.encode(original)
    decoded = rle.decode(encoded)
    print(encoded)
    print(decoded)