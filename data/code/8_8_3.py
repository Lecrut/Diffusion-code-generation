def split_and_clean(s):
    return [item.strip() for item in s.split(',') if item.strip()]

if __name__ == '__main__':
    sample = "apple, banana , , cherry,  , date"
    result = split_and_clean(sample)
    print(result)