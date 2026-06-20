def split_and_filter(text):
    return [segment.strip() for segment in text.split(',') if segment.strip()]

if __name__ == '__main__':
    sample = "apple, , banana, cherry,, , date"
    result = split_and_filter(sample)
    print(result)