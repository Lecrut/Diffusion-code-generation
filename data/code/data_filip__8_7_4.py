def split_and_filter(s):
    return [segment.strip() for segment in s.split(',') if segment.strip()]

if __name__ == '__main__':
    sample_string = "apple, , banana,  cherry , , date"
    result = split_and_filter(sample_string)
    print(result)