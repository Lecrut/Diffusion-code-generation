def fetch_nth_element(s, n):
    try:
        return s[n]
    except (IndexError, TypeError):
        if isinstance(n, int) and isinstance(s, str):
            if n < 0:
                adjusted_index = len(s) + n
                if -len(s) <= n < 0:
                    return s[adjusted_index]
            return None
        return None

if __name__ == '__main__':
    sample_string = "Hello"
    index = -1
    result = fetch_nth_element(sample_string, index)
    print(result)