def split_and_trim(input_string):
    if not input_string:
        return []
    return [part.strip() for part in input_string.split(',') if part.strip()]

if __name__ == '__main__':
    sample_data = "  apple, banana , cherry,  ,  date  , , fig "
    result = split_and_trim(sample_data)
    print(result)