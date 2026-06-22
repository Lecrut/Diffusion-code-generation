def find_min_by_length(strings):
    min_string = strings[0]
    for string in strings:
        if len(string) < len(min_string):
            min_string = string
    return min_string

if __name__ == '__main__':
    sample_values = ["sun", "moon", "stars", "comet"]
    print(find_min_by_length(sample_values))