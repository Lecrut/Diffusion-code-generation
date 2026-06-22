def split_csv_segments(csv_text):
    if not csv_text:
        return []
    segments = csv_text.split(',')
    return [s for s in segments if s]

if __name__ == '__main__':
    sample_csv = "apple,,banana, ,cherry,,date"
    result = split_csv_segments(sample_csv)
    print(result)