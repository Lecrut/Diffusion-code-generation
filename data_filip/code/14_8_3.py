def all_distinct(s):
    return len(s) == len(set(s))

if __name__ == '__main__':
    sample_string_1 = "hello"
    sample_string_2 = "world"
    print(all_distinct(sample_string_1))
    print(all_distinct(sample_string_2))