def split_commas(s):
    result = []
    start = 0
    length = len(s)
    while start < length:
        end = s.find(',', start)
        if end == -1:
            end = length
        substring = s[start:end]
        if substring:
            result.append(substring)
        start = end + 1
    return result

if __name__ == '__main__':
    sample = "apple,,banana, ,orange,,grape, "
    print(split_commas(sample))