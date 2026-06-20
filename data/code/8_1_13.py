def split_csv_meaningful(csv_string):
    segments = csv_string.split(',')
    return [segment for segment in segments if segment.strip() != '']

if __name__ == '__main__':
    sample_input = "apple,,banana,, ,cherry, ,date"
    result = split_csv_meaningful(sample_input)
    print(result)