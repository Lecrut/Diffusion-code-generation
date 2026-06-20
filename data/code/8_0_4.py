def split_commas(s):
    if not s:
        return []
    return [item for item in s.split(',') if item]

if __name__ == '__main__':
    sample = "apple,banana,,cherry, ,date"
    print(split_commas(sample))