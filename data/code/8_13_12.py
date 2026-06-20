def split_and_strip(s):
    return (part.strip() for part in s.split(',') if part.strip())

if __name__ == '__main__':
    sample = "  hello , world , , python  ,  "
    result = list(split_and_strip(sample))
    print(result)