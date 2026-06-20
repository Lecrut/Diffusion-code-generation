def split_and_filter_string(text):
    split_result = text.split(',')
    stripped_result = [item.strip() for item in split_result]
    filtered_result = [item for item in stripped_result if item]
    return filtered_result
if __name__ == '__main__':
    sample_string = 'apple, banana, , orange,  , grapefruit'
    result = split_and_filter_string(sample_string)
    print(result)