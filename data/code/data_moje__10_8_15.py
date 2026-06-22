def extract_first_item(data):
    return data[:1][0]

if __name__ == '__main__':
    sample_data = [1, "text", 3.14, True]
    result = extract_first_item(sample_data)
    print(result)