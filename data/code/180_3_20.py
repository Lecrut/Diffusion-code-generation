TOKENS = ['apple', 'banana', 'cherry', 'date', 'elderberry']
KEYWORD = 'banana'

def binary_search_keyword(keyword, tokens):
    tokens.sort()
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
    result = binary_search_keyword(KEYWORD, TOKENS)
    print(result)