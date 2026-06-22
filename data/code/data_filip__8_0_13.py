def split_commas(s):
    return [substring for substring in s.split(',') if substring.strip()]

if __name__ == '__main__':
    sample_string = "apple,  banana, , cherry,  date, , ,fig"
    result = split_commas(sample_string)
    print(result)