def split_csv_meaningful(csv_string):
    if not csv_string:
        return []
    segments = csv_string.split(',')
    return [segment for segment in segments if segment.strip()]

if __name__ == '__main__':
    test_input = ",apple,,banana,, ,cherry,,,"
    result = split_csv_meaningful(test_input)
    print(result)