def min_by_length(strings):
    return min(strings, key=len)

if __name__ == '__main__':
    sample_values = ["sun", "moon", "stars", "comet"]
    min_element = min_by_length(sample_values)
    print(min_element)