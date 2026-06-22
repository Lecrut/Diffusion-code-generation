def fetch_nth_element(string, n):
    try:
        if n < 0:
            return string[n]
        if 0 <= n < len(string):
            return string[n]
        return None
    except TypeError:
        return None
    except IndexError:
        return None

if __name__ == '__main__':
    text = "Hello, World!"
    index = 7
    negative_index = -1
    print(fetch_nth_element(text, index))
    print(fetch_nth_element(text, negative_index))
    print(fetch_nth_element(text, 100))
    print(fetch_nth_element("", 0))