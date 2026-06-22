def split_by_comma(s):
    return [item.strip() for item in s.split(',') if item.strip()]

if __name__ == '__main__':
    samples = [
        "apple, banana, cherry",
        "  orange , grape ,, kiwi  ",
        ",",
        "single",
        "   ",
        "one,two,three,four"
    ]
    for sample in samples:
        print(split_by_comma(sample))