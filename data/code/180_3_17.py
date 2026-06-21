def binary_search_keyword(keyword, tokens):
    left, right = 0, len(tokens) - 1
    while left <= right:
        mid = (left + right) // 2
        if tokens[mid] == keyword:
            return True
        elif tokens[mid] < keyword:
            left = mid + 1
        else:
            right = mid - 1
    return False

if __name__ == '__main__':
    sample_tokens = ['fig', 'grape', 'honeydew', 'kiwi', 'lemon']
    search_keyword = 'kiwi'
    print(binary_search_keyword(search_keyword, sample_tokens))