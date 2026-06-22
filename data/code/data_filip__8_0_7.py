def split_commas(data):
    if data is None:
        return []
    return [substring.strip() for substring in data.split(',') if substring.strip()]

if __name__ == '__main__':
    sample_input = "apple, banana, , cherry, ,date"
    result = split_commas(sample_input)
    print(result)
    print(len(result))
    print(result[0])
    print(result[-1])