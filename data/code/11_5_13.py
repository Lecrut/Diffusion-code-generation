def find_repeated_characters(text):
    seen = set()
    repeated = set()
    order = []
    for char in text:
        if char in seen and char not in repeated:
            repeated.add(char)
            order.append(char)
        else:
            seen.add(char)
    return order

if __name__ == '__main__':
    sample_string = "programming"
    result = find_repeated_characters(sample_string)
    print(result)