def split_csv(csv_string):
    segments = csv_string.split(',')
    meaningful_segments = [segment for segment in segments if segment]
    return meaningful_segments

if __name__ == '__main__':
    sample_csv = "apple,,banana,,cherry,,"
    result = split_csv(sample_csv)
    print(result)