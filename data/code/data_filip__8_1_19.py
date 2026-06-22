def split_csv_meaningful(csv_string):
    if not csv_string:
        return []
    return [segment for segment in csv_string.split(',') if segment]
if __name__ == '__main__':
    sample_csv = 'apple,,banana,orange,,grape,,,'
    result = split_csv_meaningful(sample_csv)
    print(result)