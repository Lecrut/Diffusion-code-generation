def split_and_filter(s):
    parts = s.split(',')
    stripped_parts = [part.strip() for part in parts]
    filtered_parts = [part for part in stripped_parts if part]
    return filtered_parts

if __name__ == '__main__':
    sample = "apple, banana,,  cherry , date"
    result = split_and_filter(sample)
    print(result)