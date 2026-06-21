def binary_search_keyword(keyword, tokens):
    tokens.sort()
    low = 0
    high = len(tokens) - 1

    while low <= high:
        mid = (low + high) // 2
        if tokens[mid] == keyword:
            return True
        elif tokens[mid] < keyword:
            low = mid + 1
        else:
            high = mid - 1

    return False

if __name__ == '__main__':
    sample_tokens = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    sample_keyword = 'banana'
    print(binary_search_keyword(sample_keyword, sample_tokens))