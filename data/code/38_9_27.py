def find_repeated_letters(input_string):
    seen = set()
    repeated = []
    for char in input_string:
        if char.isalpha() and char.lower() in seen:
            if char.lower() not in repeated:
                repeated.append(char.lower())
        else:
            seen.add(char.lower())
    return repeated

if __name__ == '__main__':
    sample_input = "Alibaba Cloud offers a wide range of AI services."
    result = find_repeated_letters(sample_input)
    print(result)