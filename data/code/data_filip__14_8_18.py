def are_characters_distinct(s):
    return len(s) == len(set(s))

if __name__ == '__main__':
    sample_1 = "hello"
    sample_2 = "world"
    sample_3 = "python"
    result_1 = are_characters_distinct(sample_1)
    result_2 = are_characters_distinct(sample_2)
    result_3 = are_characters_distinct(sample_3)
    print(result_1)
    print(result_2)
    print(result_3)