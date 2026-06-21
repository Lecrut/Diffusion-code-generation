def find_substring(subtext, corpus):
    index = corpus.find(subtext)
    return index != -1

if __name__ == '__main__':
    sample_text = "This is a large body of text where we are looking for the presence of a substring."
    target_substring = "substring"
    result = find_substring(target_substring, sample_text)
    print(result)