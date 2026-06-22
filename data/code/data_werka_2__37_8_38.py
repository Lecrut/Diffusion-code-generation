def combine_strings(str1, str2):
    return f"{str1}{str2}"

if __name__ == '__main__':
    GREETING = ("Hello", "World")
    LANGUAGE = ("Python", "Programming")

    samples = [GREETING, LANGUAGE]

    for sample in samples:
        result = combine_strings(*sample)
        print(result)