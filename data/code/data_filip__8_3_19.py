def split_and_filter(text):
    return list(filter(lambda s: s.strip() != "", text.split(",")))

if __name__ == "__main__":
    sample_data = "apple,  , banana, , orange, , , grapefruit"
    result = split_and_filter(sample_data)
    print(result)