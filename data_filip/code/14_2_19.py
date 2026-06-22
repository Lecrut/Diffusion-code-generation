def are_characters_unique(s):
    return len(set(s)) == len(s)

if __name__ == '__main__':
    sample_string = 'python'
    result = are_characters_unique(sample_string)
    print(result)