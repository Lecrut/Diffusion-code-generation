def process_strings(string_list):
    lowercase_list = []
    for s in string_list:
        lowercase_list.append(s.lower())
    return lowercase_list
if __name__ == '__main__':
    sample_list = ["Hello", "World", "Python", "Optimization"]
    result = process_strings(sample_list)
    print(result)