def split_csv_meaningful(csv_string):
    if not csv_string:
        return []
    segments = csv_string.split(',')
    return [segment for segment in segments if segment]

if __name__ == '__main__':
    sample_input = "apple,,banana,,orange,,,"
    result = split_csv_meaningful(sample_input)
    print(result)