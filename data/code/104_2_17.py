def timestamp_difference(timestamp1, timestamp2):
    return abs(timestamp1 - timestamp2)
if __name__ == '__main__':
    sample_timestamp1 = 1673904000
    sample_timestamp2 = 1672310400
    result = timestamp_difference(sample_timestamp1, sample_timestamp2)
    print(f'Timestamp difference between {sample_timestamp1} and {sample_timestamp2}: {result} seconds')